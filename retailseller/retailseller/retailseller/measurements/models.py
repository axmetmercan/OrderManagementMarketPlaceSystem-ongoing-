from statistics import mode
from django.db import models
from customer.models import CustomerInfo

# Create your models here.
ROOM_CHOICES = [
    ('SALON', 'Salon Odası'),
    ('OO', 'Oturma Odası'),
    ('MUTFAK', 'Mutfak'),
    ('YO', 'Yatak Odası'),
    ('ÇOCUK O','Çocuk Odası'),
    ('Çalışma O', 'Çalışma Odası'),
    ('GIYINME ODASI', 'Giyinme Odası'),
    ('SINEMA ODASI', 'Sinema Odası'),
    ('KILER', 'Kiler'),
    ('MISAFIR ODASI', 'Misafir Odası'),

    ]

CURTAIN_CHOICES = [
    ('ZEBRA', 'Zebra Perde'),
    ('STOR', 'Stor Perde'),
    ('DIKEY', 'Dikey Perde'),
    ('Plicel', 'Plicel Perde'),
    ('KUMAS', 'Kumaş Perde'),
    ('TÜL', 'Tül Perde'),
    ('FON', 'Fon Perde'),
    ('GUNESLİK', 'Güneşlik Perde')
]

SITUATION = [
    ('Ö Alınmadı','Ölçü Alınmadı'),
    ('Ö Alındı', 'Ölçü Alındı'),
    ('Ö Alınacak', 'Ölçü Alınacak'),
    ('S Alınmadı','Sipariş Alınmadı'),
    ('S Alındı','Sipariş Alındı'),
    ('Iptal','İptal Edildi'),
    ('Beklemede', 'Beklemede'),
    ('O Bekleniyor','Ödeme Bekleniyor')

]




class MeasuementName(models.Model):
    customer_id = models.ForeignKey(CustomerInfo, verbose_name='Müşteri ID', on_delete=models.CASCADE)
    measurement_name = models.CharField(max_length=50, verbose_name='Ölçü Adı')
    situation = models.CharField(max_length=50, verbose_name='Durumu', choices=SITUATION,null=True, blank=True,default='Ö Alınacak')
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name ='Ölçü Adı'
        verbose_name_plural = 'Ölçü Adları'


    def __str__(self):
        return self.measurement_name
        


class Measurement(models.Model):
    customer_id = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE, verbose_name='Müşteri IDs')
    measurement_id = models.ForeignKey(MeasuementName, on_delete=models.CASCADE, verbose_name='Ölçü ID')
    room_name = models.CharField(max_length=15, choices=ROOM_CHOICES, verbose_name='Oda Adı')
    curtain_type = models.CharField(max_length=15, choices=CURTAIN_CHOICES, verbose_name='Perde Tipi')
    width = models.DecimalField(decimal_places=1, max_digits=4, null=True, verbose_name='En')
    height = models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Boy', null=True)
    note = models.CharField(max_length=250, verbose_name='Ölçü Notu', null=True, blank=True)
    window_picture = models.FileField(verbose_name='Pencere Resmi', upload_to='images/window_images', blank=False,null=False)
    class Meta:
        verbose_name='Ölçü'
        verbose_name_plural = 'Ölçüler'

    def __str__(self):
        return str(self.measurement_id)



     


