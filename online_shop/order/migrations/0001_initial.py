# Generated by Django 4.0.2 on 2022-02-22 01:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('discount_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.offcode')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
