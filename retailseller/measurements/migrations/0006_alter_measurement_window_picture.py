# Generated by Django 4.0.1 on 2022-02-11 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0005_alter_measurement_window_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='window_picture',
            field=models.FileField(blank=True, upload_to='images/window_images', verbose_name='Pencere Resmi'),
        ),
    ]
