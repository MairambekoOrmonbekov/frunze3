# Generated by Django 4.2.1 on 2023-05-04 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_category_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='uploaded',
            field=models.DateTimeField(auto_now=True, verbose_name='Изменен'),
        ),
    ]