from dashboard.models import HomeDetails
from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Testimonials(models.Model):
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    quote = models.TextField()

    class Meta:
        verbose_name_plural = 'Testimonials'


class Subscribe(models.Model):
    email = models.EmailField(unique=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Subscribe'


class BusinessData(models.Model):
    data = models.ForeignKey('dashboard.Navbar', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'BusinessData'


class HomeSlideImg(models.Model):
    images = models.OneToOneField(HomeDetails, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'HomeSlideImg'
