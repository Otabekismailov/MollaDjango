# Generated by Django 4.2 on 2023-04-25 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0016_cart_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=250)),
                ('house_number', models.IntegerField()),
                ('city', models.CharField(max_length=250)),
                ('index', models.IntegerField()),
                ('phone', models.CharField(max_length=250)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_cart', to='polls.cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]