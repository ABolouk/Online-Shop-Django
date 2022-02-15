# Generated by Django 4.0.2 on 2022-02-15 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_category_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discount',
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.discount'),
        ),
    ]