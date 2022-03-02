from django.contrib import admin
from .models import Product, Variant

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['brand', 'code', 'category', 'head_name']
    search_fields = ['code']
    list_filter = ['brand', 'category', 'head_name']
    class Meta:
        model =Product


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display =['product','code' ]
    list_filter = ['product']
    search_fields =['product','code']
    class Meta:
        model = Variant