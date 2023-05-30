# Generated by Django 4.2.1 on 2023-05-21 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_category_product_category'),
        ('user', '0004_register_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('det', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.register')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
    ]
