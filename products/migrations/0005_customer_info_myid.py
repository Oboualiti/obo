# Generated by Django 4.1.7 on 2023-03-12 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_customer_info_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_info',
            name='myid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]