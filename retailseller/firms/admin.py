from pyexpat import model
from statistics import mode
from django.contrib import admin
from .models import Categories, Firm, Head
from .models import Product, Variant

# Register your models here.

@admin.register(Firm)
class FirmAdmin(admin.ModelAdmin):
    list_display =['name']    
    search_fields = ['name']
    list_display_links = ['name']
    class Meta:
        model = Firm

@admin.register(Head)
class HeadAdmin(admin.ModelAdmin):
    list_display = ['name', 'firm']
    list_display_links = ['name']
    list_filter = ['firm']
    class Meta:
        model = Head




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['code', 'category', 'head_name']
    search_fields = ['code']
    list_filter = ['category', 'head_name']
    class Meta:
        model =Product


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display =['product','variant_code' ]
    list_filter = ['product']
    search_fields =['product','variant_code']
    class Meta:
        model = Variant


admin.site.register(Categories)