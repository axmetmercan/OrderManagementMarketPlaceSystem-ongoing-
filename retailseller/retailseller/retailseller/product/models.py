from django.db import models

# Create your models here.

class Product(models.Model):
    brand = models.CharField(max_length=100, verbose_name = 'Marka', blank=False, null=False)
    head_name = models.CharField(max_length=100, verbose_name = 'Başlık Adı', blank=True, null=True)
    code = models.CharField(max_length=100, verbose_name='Kodu', blank=False, null=False)
    category = models.CharField(max_length=100, verbose_name='Kategori', blank=False, null=False)
    color = models.CharField(max_length=100, verbose_name='Renk', blank=True, null=True)
    width = models.DecimalField(decimal_places=0, max_digits=3, verbose_name='En' blank=True, null=True)
    max_width = models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Max Ayarlanbilir En', blank=True, null=True)
    unit_price = models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Fiyat', blank=True, null=True)
    picture = models.FileField(blank=True, null=True, verbose_name='Resim')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Tarih')
    

    def __str__(self):
        return self.code


    class Meta:
        ordering = ['-created_date']
    
class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Ürün ID')
    code = models.CharField(max_length=100, verbose_name='Varyant Kodu',)

    def __str__(self):
        return self.code