# Generated by Django 4.2 on 2023-04-23 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_product_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='subtotal',
            field=models.IntegerField(default=0),
        ),
    ]