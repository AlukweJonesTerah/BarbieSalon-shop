from dashboard.models import HomeDetails, Navbar, AboutUs, Menu, SpecialOfferTable, WorkingHoursTable, Brands, \
    ReviewsSubtitle, NewsLetters
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import SubscribeForm


# Create your views here.
def index(request):
    images = HomeDetails.objects.all()
    navbars = Navbar.objects.all()
    abouts = AboutUs.objects.all()
    menus = Menu.objects.all()
    offers = SpecialOfferTable.objects.all()
    workhours = WorkingHoursTable.objects.all()
    brands = Brands.objects.all()
    reviews = ReviewsSubtitle.objects.all()
    newsletters = NewsLetters.objects.all()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'You Have Successful Subscribed To Our Newsletters We Will Be Glad To \
            Be Updating You. Thank You ')
            return redirect('/')
        else:
            messages.error(request, 'We are sorry but this email has already subscribed to our newsletter ! ')

    else:

        form = SubscribeForm()

    context = {
        'images': images,
        'navbars': navbars,
        'abouts': abouts,
        'menus': menus,
        'offers': offers,
        'workhours': workhours,
        'brands': brands,
        'reviews': reviews,
        'newsletters': newsletters,
        'form': form,
    }

    return render(request, 'CustomerView/view/CustomerView-index.html', context)
