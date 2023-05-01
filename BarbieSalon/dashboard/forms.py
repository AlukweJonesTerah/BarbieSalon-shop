from django import forms
from django.core.validators import MaxLengthValidator

from .models import Product, Order, MailMessageSending, Navbar, HomeDetails, AboutUs, Menu, SpecialOfferTable, \
    WorkingHoursTable, Brands, NewsLetters, ReviewsSubtitle


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'order_quantity']


class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessageSending
        fields = '__all__'


class NavbarForm(forms.ModelForm):
    class Meta:
        model = Navbar
        fields = ['business_name', 'phone_number']
        validators = [
            MaxLengthValidator(1,
                               message='A maximum of 1 business name and phone_number. If you want to change either delete or edit ')
        ]


class HomeDetailsForm(forms.ModelForm):
    class Meta:
        model = HomeDetails
        fields = ['homeimage', 'subtitle', 'hometitle1', 'hometitle2']
        validators = [
            MaxLengthValidator(5,
                               message='A maximum of 5 images. If you want to change either delete or edit ')
        ]


class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = ['aboutimg', 'aboutuscaption', 'subtitle', 'title1', 'title2', 'description']
        validators = [
            MaxLengthValidator(1,
                               message='A maximum of 1 about. If you want to change either delete or edit ')
        ]


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['subtitle', 'title', 'description']
        validators = [
            MaxLengthValidator(1,
                               message='A maximum of 1 instance can be added. If you want to change either delete or edit ')
        ]


class SpecialOfferForm(forms.ModelForm):
    class Meta:
        model = SpecialOfferTable
        fields = ['hairstyleimage', 'hairstylename', 'description', 'discountPrice', 'initialprice']
        validators = [
            MaxLengthValidator(3,
                               message='A maximum of 3 instance can be added. If you want to change either delete or edit ')
        ]


class WorkingHoursForm(forms.ModelForm):
    class Meta:
        model = WorkingHoursTable
        fields = ['day', 'time']
        validators = [
            MaxLengthValidator(7,
                               message='A maximum of 7 instance can be added. If you want to change either delete or edit ')
        ]


class BrandsForm(forms.ModelForm):
    class Meta:
        model = Brands
        fields = ['brandimage']


class ReviewsSubtitleForm(forms.ModelForm):
    class Meta:
        model = ReviewsSubtitle
        fields = ['subtitle', 'title', 'description']
        validators = [
            MaxLengthValidator(1,
                               message='A maximum of 1 instance can be added. If you want to change either delete or edit ')
        ]


class NewsLettersForm(forms.ModelForm):
    class Meta:
        model = NewsLetters
        fields = ['newsletter_description']
        validators = [
            MaxLengthValidator(1,
                               message='A maximum of 1 instance can be added. If you want to change either delete or edit ')
        ]
