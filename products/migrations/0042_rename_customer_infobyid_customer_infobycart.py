# Generated by Django 3.2.19 on 2023-06-28 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0041_customer_infobyid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer_infobyId',
            new_name='Customer_infobycart',
        ),
    ]
