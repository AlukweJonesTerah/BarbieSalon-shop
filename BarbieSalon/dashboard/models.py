from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.

CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)

    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return f'{self.customer}-{self.name}'


class MailMessageSending(models.Model):
    tittle = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    class Meta:
        verbose_name_plural = 'MailMessageSending'

    def __str__(self):
        return self.tittle


class Subscribers(models.Model):
    emails = models.ForeignKey('CustomerView.Subscribe', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Subscribers'


class Navbar(models.Model):
    business_name = models.CharField(max_length=25)
    phone_number = models.PositiveBigIntegerField(unique=True, blank=False, null=False)

    class Meta:
        verbose_name_plural = 'Navbar'

    def clean(self):
        if Navbar.objects.count() >= 1 and self.pk is None:
            raise ValidationError(
                "Can only create 1 Navbar instance. Try editing/removing one of the existing instance.")


class Service(models.Model):
    file = models.CharField(max_length=20)
    icon = models.CharField(max_length=30)
    heading = models.CharField(max_length=100)
    paragraph = models.CharField(max_length=10000)


class HomeDetails(models.Model):
    homeimage = models.ImageField(upload_to='home_images')
    subtitle = models.CharField(max_length=100)
    hometitle1 = models.CharField(max_length=50)
    hometitle2 = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'HomeDetails'

    def clean(self):
        if Navbar.objects.count() >= 5 and self.pk is None:
            raise ValidationError(
                "Can only create 5 images instances. Try editing/removing one of the existing instance.")


class AboutUs(models.Model):
    aboutimg = models.ImageField(upload_to='aboutus_img')
    aboutuscaption = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=50)
    title1 = models.CharField(max_length=50)
    title2 = models.CharField(max_length=50)
    description = models.CharField(max_length=1000000)

    def clean(self):
        if AboutUs.objects.count() >= 1 and self.pk is None:
            raise ValidationError(
                "Can only create 1 AboutUs instance. Try editing/removing one of the existing instance.")


class Menu(models.Model):
    subtitle = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=400)

    def clean(self):
        if Menu.objects.count() >= 1 and self.pk is None:
            raise ValidationError(
                "Can only create one Menu instance. Try editing/removing one of the existing instance.")


class SpecialOfferTable(models.Model):
    hairstyleimage = models.ImageField(upload_to='specialoffer_image')
    hairstylename = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    discountPrice = MoneyField(max_digits=7, decimal_places=2, default_currency='KSH')
    initialprice = MoneyField(max_digits=7, decimal_places=2, default_currency='KSH')

    def clean(self):
        if SpecialOfferTable.objects.count() >= 3 and self.pk is None:
            raise ValidationError(
                "Can only create 3 SpecialOfferTable instance. Try editing/removing one of the existing instance.")


class WorkingHoursTable(models.Model):
    day = models.CharField(max_length=9)
    time = models.CharField(max_length=16)

    def clean(self):
        if WorkingHoursTable.objects.count() >= 7 and self.pk is None:
            raise ValidationError(
                "Can only create 1 WorkingHoursTable instance. Try editing/removing one of the existing instance.")


class Brands(models.Model):
    brandimage = models.ImageField(upload_to='brands_images')


class ReviewsSubtitle(models.Model):
    subtitle = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=10000)

    def clean(self):
        if ReviewsSubtitle.objects.count() >= 1 and self.pk is None:
            raise ValidationError(
                "Can only create one ReviewsSubtitle instance. Try editing/removing one of the existing instance.")


class NewsLetters(models.Model):
    objects = None
    newsletter_description = models.CharField(max_length=200)

    def clean(self):
        if NewsLetters.objects.count() >= 1 and self.pk is None:
            raise ValidationError(
                "Can only create one NewsLetters instance. Try editing/removing one of the existing instance.")
