# Generated by Django 4.0.2 on 2022-02-15 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_offcode'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='discount_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.offcode'),
        ),
    ]