# Generated by Django 4.1.7 on 2023-03-18 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_delete_emails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_info',
            name='city',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='customer_info',
            name='full_name',
            field=models.CharField(max_length=30),
        ),
    ]
