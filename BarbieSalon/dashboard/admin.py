from django.contrib import admin
from .models import Product, Order, Navbar, HomeDetails

# Register your models here.

admin.site.site_header = 'Barbie Salon Admin Panel'

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Navbar)
admin.site.register(HomeDetails)