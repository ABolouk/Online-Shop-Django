# Generated by Django 4.0.2 on 2022-02-15 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_category_categories_category_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='max_value',
            field=models.CharField(max_length=20, null=True),
        ),
    ]