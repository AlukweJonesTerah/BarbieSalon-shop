from django.conf import settings
from django.contrib import messages
from users.models import CustomUser
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django_pandas.io import read_frame
from django.contrib.auth import get_user_model

from .forms import ProductsForm, OrderForm, MailMessageForm, NavbarForm, HomeDetailsForm, AboutUsForm, MenuForm, \
    SpecialOfferForm, WorkingHoursForm, BrandsForm, ReviewsSubtitleForm, NewsLettersForm
from .models import Product, Order, Subscribers, Navbar, HomeDetails, AboutUs, Menu, SpecialOfferTable, \
    WorkingHoursTable, Brands, ReviewsSubtitle, NewsLetters


# Create your views here.

def index(request):
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    customer = get_user_model().objects.filter(groups=2)
    customer_count = customer.count()

    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            redirect('dashboard-index')

    else:
        form = OrderForm()

    context = {
        'form': form,
        'order': order,
        'product': product,
        'product_count': product_count,
        'order_count': order_count,
        'customer_count': customer_count,
    }
    return render(request, 'dashboard/usermanage/index.html', context)


def products(request):
    product = Product.objects.all()
    product_count = product.count
    customer = CustomUser.objects.filter(groups=2)
    customer_count = customer.count()
    order = Order.objects.all()
    order_count = order.count()
    product_quantity = Product.objects.filter(name='')
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-products')

    else:
        form = ProductsForm()

    context = {
        'product': product,
        'form': form,
        'customer': customer,
        'product_count': product_count,
        'customer_count': customer_count,
        'order_count': order_count,
        'product_quantity': product_quantity,
    }
    return render(request, 'dashboard/usermanage/products.html', context)


def product_detail(request, pk):
    context = {

    }
    return render(request, 'dashboard/usermanage/products_details.html', context)


def product_edit(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else:
        form = ProductsForm(instance=item)

    context = {
        'form': form,
        'item': item,
    }
    return render(request, 'dashboard/usermanage/products_edit.html', context)


def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-products')
    context = {
        'item': item,
    }
    return render(request, 'dashboard/usermanage/products_delete.html', context)


def customers(request):
    customer = CustomUser.objects.filter(groups=2)
    customer_count = customer.count()
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    context = {
        'customer': customer,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/usermanage/customers.html', context)


def customer_detail(request, pk):
    customer = CustomUser.objects.filter(groups=2)
    customer_count = customer.count()
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    customer = CustomUser.objects.get(id=pk)
    context = {
        'customer': customer,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/usermanage/customers_detail.html', context)


def order(request):
    order = Order.objects.all()
    order_count = order.count()
    customer = CustomUser.objects.filter(groups=2)
    customer_count = customer.count()
    product = Product.objects.all()
    product_count = product.count()

    context = {
        'order': order,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/usermanage/order.html', context)


def mail_sending(request):
    emails = Subscribers.objects.all()
    df = read_frame(emails, fieldnames=['name'])
    mail_list = df['email'].values.tolist()
    print(mail_list)
    if request.method == 'POST':
        form = MailMessageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            tittle = form.cleaned_data.get('tittle')
            message = form.cleaned_data.get('message')
            email_from = settings.EMAIL_HOST_USER
            send_mail(
                tittle,
                message,
                email_from,
                mail_list,
                fail_silently=True,
            )
            messages.success(request, 'Message has been sent to the Mail List')
            return redirect('dashboard-mail_sending')

        else:
            form = MailMessageForm()

        context = {
            'form': form,
        }
        return render(request, 'dashboard/mail_sending.html', context)


def navbar_customize(request):
    navbar = Navbar.objects.all()
    if request.method == 'POST':
        form = NavbarForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            redirect('dashboard-navbar_customize')

    else:
        form = NavbarForm()

    context = {
        'form': form,
        'navbar': navbar,
    }
    return render(request, 'dashboard/homeview-manage/navbar_customize.html', context)


def navbar_customize_edit(request, pk):
    details = Navbar.objects.get(id=pk)
    if request.method == 'POST':
        form = NavbarForm(request.POST, request.FILES, instance=details)
        if form.is_valid():
            form.save()
            return redirect('dashboard-navbar_customize')
    else:
        form = NavbarForm(instance=details)

    context = {
        'form': form,
        'details': details,
    }
    return render(request, 'dashboard/homeview-manage/navbar_customize_edit.html', context)


def navbar_customize_delete(request, pk):
    details = Navbar.objects.get(id=pk)
    if request.method == 'POST':
        details.delete()
        return redirect('dashboard-navbar_customize')
    context = {
        'details': details,
    }
    return render(request, 'dashboard/homeview-manage/navbar_customize_delete.html', context)


def homedetails_customize(request):
    home = HomeDetails.objects.all()
    if request.method == 'POST':
        h_form = HomeDetailsForm(request.POST, request.FILES)
        if h_form.is_valid():
            obj = h_form.save()
            obj.save()
            messages.success(request, 'Your successfully added a home image.')
            redirect('dashboard-homedetails_customize')

    else:
        h_form = HomeDetailsForm()

    context = {
        'h_form': h_form,
        'home': home,
    }
    return render(request, 'dashboard/homeview-manage/homedetails_customize.html', context)


def homedetails_customize_edit(request, pk):
    homeupdate = HomeDetails.objects.get(id=pk)
    if request.method == 'POST':
        h_form = HomeDetailsForm(request.POST, request.FILES, instance=homeupdate)
        if h_form.is_valid():
            h_form.save()
            messages.success(request, 'You have successfully updated home image ')
            return redirect('dashboard-homedetails_customize')
    else:
        h_form = HomeDetailsForm(instance=homeupdate)

    context = {
        'h_form': h_form,
        'homeupdate': homeupdate,
    }
    return render(request, 'dashboard/homeview-manage/homedetails_customize_edit.html', context)


def homedetails_customize_delete(request, pk):
    home_image = HomeDetails.objects.get(id=pk)
    if request.method == 'POST':
        home_image.delete()
        return redirect('dashboard-homedetails_customize')
    context = {
        'home_image': home_image,
    }
    return render(request, 'dashboard/homeview-manage/homedetails_customize_delete.html', context)


def about_customize(request):
    about = AboutUs.objects.all()
    if request.method == 'POST':
        form = AboutUsForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            messages.success(request, 'Your successfully added "About" info.')
            redirect('dashboard-about_customize')

    else:
        form = AboutUsForm()

    context = {
        'form': form,
        'about': about,
    }
    return render(request, 'dashboard/homeview-manage/about_customize.html', context)


def about_customize_edit(request, pk):
    aboutdata = AboutUs.objects.get(id=pk)
    if request.method == 'POST':
        form = AboutUsForm(request.POST, request.FILES, instance=aboutdata)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated "About" info')
            return redirect('dashboard-about_customize')
    else:
        form = AboutUsForm(instance=aboutdata)

    context = {
        'form': form,
        'aboutdata': aboutdata,
    }
    return render(request, 'dashboard/homeview-manage/about_customize_edit.html', context)


def about_customize_delete(request, pk):
    aboutdata = AboutUs.objects.get(id=pk)
    if request.method == 'POST':
        aboutdata.delete()
        return redirect('dashboard-about_customize')
    context = {
        'aboutdata': aboutdata,
    }
    return render(request, 'dashboard/homeview-manage/about_customize_delete.html', context)


def menu_customize(request):
    menu = Menu.objects.all()
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            messages.success(request, 'Your successfully added "Menu" info.')
            redirect('dashboard-menu_customize')

    else:
        form = MenuForm()

    context = {
        'form': form,
        'menu': menu,
    }
    return render(request, 'dashboard/homeview-manage/menu_customize.html', context)


def menu_customize_edit(request, pk):
    menudata = Menu.objects.get(id=pk)
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES, instance=menudata)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated "Menu" info')
            return redirect('dashboard-menu_customize')
    else:
        form = MenuForm(instance=menudata)

    context = {
        'form': form,
        'menudata': menudata,
    }
    return render(request, 'dashboard/homeview-manage/menu_customize_edit.html', context)


def menu_customize_delete(request, pk):
    menudata = Menu.objects.get(id=pk)
    if request.method == 'POST':
        menudata.delete()
        return redirect('dashboard-menu_customize')
    context = {
        'menudata': menudata,
    }
    return render(request, 'dashboard/homeview-manage/menu_customize_delete.html', context)


def offer_customize(request):
    offer = SpecialOfferTable.objects.all()
    if request.method == 'POST':
        form = SpecialOfferForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            messages.success(request, 'Your successfully added "Special Offer" info.')
            redirect('dashboard-offer_customize')

    else:
        form = SpecialOfferForm()

    context = {
        'form': form,
        'offer': offer,
    }
    return render(request, 'dashboard/homeview-manage/offer_customize.html', context)


def offer_customize_edit(request, pk):
    offerdata = SpecialOfferTable.objects.get(id=pk)
    if request.method == 'POST':
        form = SpecialOfferForm(request.POST, request.FILES, instance=offerdata)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated "Special Offer" info')
            return redirect('dashboard-offer_customize')
    else:
        form = SpecialOfferForm(instance=offerdata)

    context = {
        'form': form,
        'offerdata': offerdata,
    }
    return render(request, 'dashboard/homeview-manage/offer_customize_edit.html', context)


def offer_customize_delete(request, pk):
    offerdata = SpecialOfferTable.objects.get(id=pk)
    if request.method == 'POST':
        offerdata.delete()
        return redirect('dashboard-offer_customize')
    context = {
        'offerdata': offerdata,
    }
    return render(request, 'dashboard/homeview-manage/offer_customize_delete.html', context)


def work_customize(request):
    work = WorkingHoursTable.objects.all()
    if request.method == 'POST':
        form = WorkingHoursForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            messages.success(request, 'Your successfully added "Working Time" info.')
            redirect('dashboard-work_customize')

    else:
        form = WorkingHoursForm()

    context = {
        'form': form,
        'work': work,
    }
    return render(request, 'dashboard/homeview-manage/work_customize.html', context)


def work_customize_edit(request, pk):
    workdata = WorkingHoursTable.objects.get(id=pk)
    if request.method == 'POST':
        form = WorkingHoursForm(request.POST, request.FILES, instance=workdata)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated "Working Hours" info')
            return redirect('dashboard-work_customize')
    else:
        form = SpecialOfferForm(instance=workdata)

    context = {
        'form': form,
        'workdata': workdata,
    }
    return render(request, 'dashboard/homeview-manage/work_customize_edit.html', context)


def work_customize_delete(request, pk):
    workdata = WorkingHoursTable.objects.get(id=pk)
    if request.method == 'POST':
        workdata.delete()
        return redirect('dashboard-work_customize')
    context = {
        'workdata': workdata,
    }
    return render(request, 'dashboard/homeview-manage/work_customize_delete.html', context)


def brand_customize(request):
    brand = Brands.objects.all()
    if request.method == 'POST':
        form = BrandsForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            messages.success(request, 'Your successfully added "Brand" info.')
            redirect('dashboard-brand_customize')

    else:
        form = BrandsForm()

    context = {
        'form': form,
        'brand': brand,
    }
    return render(request, 'dashboard/homeview-manage/brand_customize.html', context)


def brand_customize_edit(request, pk):
    branddata = Brands.objects.get(id=pk)
    if request.method == 'POST':
        form = BrandsForm(request.POST, request.FILES, instance=branddata)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated "Brand" info')
            return redirect('dashboard-brand_customize')
    else:
        form = BrandsForm(instance=branddata)

    context = {
        'form': form,
        'branddata': branddata,
    }
    return render(request, 'dashboard/homeview-manage/brand_customize_edit.html', context)


def brand_customize_delete(request, pk):
    branddata = Brands.objects.get(id=pk)
    if request.method == 'POST':
        branddata.delete()
        return redirect('dashboard-brand_customize')
    context = {
        'branddata': branddata,
    }
    return render(request, 'dashboard/homeview-manage/brand_customize_delete.html', context)


def reviews_customize(request):
    review = ReviewsSubtitle.objects.all()
    if request.method == 'POST':
        form = ReviewsSubtitleForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            messages.success(request, 'Your successfully added "Review" info.')
            redirect('dashboard-reviews_customize')

    else:
        form = ReviewsSubtitleForm()

    context = {
        'form': form,
        'review': review,
    }
    return render(request, 'dashboard/homeview-manage/reviews_customize.html', context)


def reviews_customize_edit(request, pk):
    reviewdata = ReviewsSubtitle.objects.get(id=pk)
    if request.method == 'POST':
        form = ReviewsSubtitleForm(request.POST, request.FILES, instance=reviewdata)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated "Review" info')
            return redirect('dashboard-reviews_customize')
    else:
        form = ReviewsSubtitleForm(instance=reviewdata)

    context = {
        'form': form,
        'reviewdata': reviewdata,
    }
    return render(request, 'dashboard/homeview-manage/reviews_customize_edit.html', context)


def reviews_customize_delete(request, pk):
    reviewdata = ReviewsSubtitle.objects.get(id=pk)
    if request.method == 'POST':
        reviewdata.delete()
        return redirect('dashboard-reviews_customize')
    context = {
        'reviewdata': reviewdata,
    }
    return render(request, 'dashboard/homeview-manage/reviews_customize_delete.html', context)


def newsletter_customize(request):
    newsletter = NewsLetters.objects.all()
    if request.method == 'POST':
        form = NewsLettersForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            messages.success(request, 'Your successfully added "Newsletter" info.')
            redirect('dashboard-newsletter_customize')

    else:
        form = NewsLettersForm()

    context = {
        'form': form,
        'newsletter': newsletter,
    }
    return render(request, 'dashboard/homeview-manage/newsletter_customize.html', context)


def newsletter_customize_edit(request, pk):
    newsletterdata = NewsLetters.objects.get(id=pk)
    if request.method == 'POST':
        form = NewsLettersForm(request.POST, request.FILES, instance=newsletterdata)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated "Newsletter" info')
            return redirect('dashboard-brand_customize')
    else:
        form = NewsLettersForm(instance=newsletterdata)

    context = {
        'form': form,
        'newsletterdata': newsletterdata,
    }
    return render(request, 'dashboard/homeview-manage/newsletter_customize_edit.html', context)


def newsletter_customize_delete(request, pk):
    newsletterdata = NewsLetters.objects.get(id=pk)
    if request.method == 'POST':
        newsletterdata.delete()
        return redirect('dashboard-newsletter_customize')
    context = {
        'newsletterdata': newsletterdata,
    }
    return render(request, 'dashboard/homeview-manage/newsletter_customize_delete.html', context)
