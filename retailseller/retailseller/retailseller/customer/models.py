from operator import mod
from os import name
from pyexpat import model
from statistics import mode
from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

INVOINCE_CHOICES = [
    ('B', 'Bireysel'),
    ('K', 'Kurumsal'),
]



PILE_CHOICES = [
    ('SEYREK', 'Seyrek Pile'),
    ('Orta', 'Orta Pile'),
    ('SIK', 'Sık Pile'),
    ('PILESIZ', 'Pilesiz'),
    ('KRUVAZE', 'Kruvaze'),
    ('TUL BRIZ','Tül Briz Perde'),
    ('Zebra BRIZ','Zebra Briz Perde')
    ]



class CustomerInfo(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Firma Personeli', blank=True, null=True)
    name = models.CharField(max_length=200, verbose_name='Adı')
    surname = models.CharField(max_length=200, verbose_name='Soyisim')
    phone = PhoneNumberField()
    email = models.EmailField(max_length=200, verbose_name='email', default=None)
    invoince_type = models.CharField(default=False, max_length=1, choices=INVOINCE_CHOICES, verbose_name='Fatura Tipi' )
    turkish_id = models.IntegerField(default='11111111111', blank=True, null=True, verbose_name='TC Kimlik No:')
    tax_id = models.IntegerField(default=None, blank=True, null=True, verbose_name='VKN No')
    tax_name = models.CharField(max_length=200,default=None, blank=True, null=True, verbose_name='Fatura Müşteri Adı')
    tax_surname = models.CharField(max_length=200,default=None, blank=True, null=True,verbose_name='Fatura Müşteri Soyadı')
    tax_office = models.CharField(max_length=200,default=None, blank=True, null=True, verbose_name='Vergi Dairesi')
    tax_title = models.CharField(max_length=200,default=None, blank=True, null=True, verbose_name='Firma Ünvanı')
    invoince_address = models.TextField(max_length=500,default=None, blank=False, null=False, verbose_name='Fatura Adresi')
    created_time = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Üyelik Zamanı', editable=True)


    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name', 'surname']
        verbose_name = 'Müşteri Bilgisi'
        verbose_name_plural = 'Müşteri Bilgileri'
