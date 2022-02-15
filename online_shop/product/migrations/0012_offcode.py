# Generated by Django 4.0.2 on 2022-02-15 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_category_category_alter_category_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='OffCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('PER', 'Percentage Discount'), ('VAL', 'Value Discount')], max_length=3)),
                ('amount', models.CharField(max_length=20)),
                ('max_value', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]