from django.contrib import admin
from .models import Product
admin.site.site_header='CUSTOME ADMIN PANEL'
admin.site.site_title='custom pannel'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


