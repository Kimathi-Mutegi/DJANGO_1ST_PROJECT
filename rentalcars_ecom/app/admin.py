from django.contrib import admin
from . models import Product, Customer
# Register your models here.
@admin.register(Product)
class Productmodeladmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price', 'category', 'products_image', ]

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'town', 'county','zipcode' ]