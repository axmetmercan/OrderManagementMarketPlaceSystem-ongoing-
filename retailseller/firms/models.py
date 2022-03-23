from datetime import datetime
from select import select
from statistics import mode
from tabnanny import verbose
from tkinter import ttk
from tkinter.messagebox import NO
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Categories(models.Model):
    
    category = models.CharField(max_length=100, verbose_name='Ürün Kategorisi')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural ="Kategoriler"

class Firm(models.Model):
    #user stands for the who saved the firm first.
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Firma Personeli', blank=True, null=True)
    name = models.CharField(max_length=100, null=False,blank=False, verbose_name="Firma Adı")
    salesmanan = models.CharField(max_length=100, blank=False, verbose_name = 'Pazaralamacı Adı')
    salesman_phone = PhoneNumberField(verbose_name ='Pazarlamacı Tel')
    order_phone = PhoneNumberField(verbose_name = 'Sipariş Hattı')
    email = models.EmailField(verbose_name='E-mail', blank=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Tarih', blank=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Firma"
        verbose_name_plural = "Firmalar "

    

class Head(models.Model):
    firm = models.ForeignKey('Firm', on_delete=models.CASCADE, verbose_name='Firma Adı')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Firma Personeli', blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name='Başlık ismi')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Tarih', blank=True)

    
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Başlık"
        verbose_name_plural = "Başlıklar"    




class Product(models.Model):
    brand = models.ForeignKey(Firm, on_delete=models.CASCADE, verbose_name='Firma adı', blank=True, null=True)
    head_name = models.ForeignKey(Head, on_delete=models.CASCADE, verbose_name = 'Başlık Adı', blank=True, null=True)
    code = models.CharField(max_length=100, verbose_name='Kodu', blank=False, null=False)
    default_variant = models.CharField(max_length=100, verbose_name='Varsayılan Varyant Kodu', blank=False, null=False, default=1)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name="Kategorisi")
    color = models.CharField(max_length=100, verbose_name='Renk', blank=True, null=True)
    width = models.DecimalField(decimal_places=0, max_digits=3, verbose_name='En', blank=True, null=True)
    max_width = models.DecimalField(decimal_places=0, max_digits=3, verbose_name='Max Ayarlanbilir En', blank=True, null=True)
    unit_price = models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Fiyat', blank=True, null=True)
    picture = models.FileField(blank=True, null=True, verbose_name='Ürün Resmi', upload_to='images/product_images')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Tarih')
    

    def __str__(self):
        return self.code


    class Meta:
        ordering = ['-created_date']
        verbose_name = "Ürün"    
        verbose_name_plural = "Ürünler"



class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Ürün ID')
    variant_code = models.CharField(max_length=100, verbose_name='Varyant Kodu',)
    variant_unit_price = models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Fiyat', blank=True, null=True)

    def __str__(self):
        return self.code

    class Meta:
            
        verbose_name = "Varyant"    
        verbose_name_plural = "Varyantlar"

