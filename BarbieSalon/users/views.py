from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.translation import gettext as _

from .decorators import user_not_authenticated
from .forms import UserRegistrationForm, UserLoginForm, UserUpdateForm
from .tokens import account_activation_token


@permission_required('auth.is_admin')
def change_user_status(request, user_id):
    # Get the user object and the new status
    user = get_user_model().objects.get(pk=user_id)
    new_status = request.POST.get('status')
    # Remove the user from their current group
    user.groups.clear()
    # Add the user to the new group
    if new_status == 'admin':
        group = Group.objects.get_or_create(name='admin')
    elif new_status == 'staff':
        group = Group.objects.get_or_create(name='staff')
    else:
        group = Group.objects.get_or_create(name='customer')
    group.user_set.add(user)
    # Save the user object
    user.save()
    return redirect('users-list')

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except(TypeError, ValueError):
        user = None
        messages.error(request, _("Invalid activation link"))
    except User.DoesNotExist:
        user = None
        messages.error(request, _("User doest not exist"))

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True

        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('users-login')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('users-email_activation_error')


def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear {user}, please go to you email {to_email} inbox and click on \
                received activation link to confirm and complete the registration. Note: Check your spam folder.')
    else:
        messages.error(request,
                       f'There was a Problem sending email to {to_email}. Please check if you typed it correctly.')


def email_activation_error(request):
    return render(request, 'users/invalid_confirmation.html')


@user_not_authenticated
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            group, created = Group.objects.get_or_create(name='customers')
            group.user_set.add(user)
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('users-confirmation_sent')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name="users/register.html",
        context={"form": form}
    )


def confirmation_sent(request):
    return render(request, 'users/confirmation_sent.html')


@login_required
def custom_logout(request):
    logout(request)

    return render(request, 'users/logout.html', messages.info(request, "Logged out successfully!"))


@user_not_authenticated
def custom_login(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello {user.username}! You have been logged in")
                if user.is_superuser and user.is_staff:
                    return redirect("dashboard-index")
                elif user.is_active:
                    return redirect("CustomerView-index")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue

                messages.error(request, error)

    form = UserLoginForm()

    return render(
        request=request,
        template_name="users/login.html",
        context={"form": form}
    )


@login_required
def profile(request, username):
    if request.method == "POST":
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()
            messages.success(request, f'{user_form.username}, Your profile has been updated!')
            return redirect("profile", user_form.username)

        for error in list(form.errors.values()):
            messages.error(request, error)

    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        form.fields['description'].widget.attrs = {'rows': 1}
        return render(
            request=request,
            template_name="users/profile.html",
            context={"form": form}
        )

    return redirect("dashboard-index")
