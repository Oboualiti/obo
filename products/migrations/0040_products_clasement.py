# Generated by Django 3.2.19 on 2023-06-25 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0039_auto_20230601_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='clasement',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
