# Generated by Django 4.1.7 on 2023-04-04 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField(verbose_name='jalpy baasy')),
                ('created_at', models.DateField(auto_now=True)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('ordered_items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
    ]
