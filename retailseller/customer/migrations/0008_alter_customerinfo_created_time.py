# Generated by Django 4.0.1 on 2022-02-04 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_customerinfo_created_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerinfo',
            name='created_time',
            field=models.DateTimeField(auto_created=True, auto_now_add=True, null=True),
        ),
    ]
