# Generated by Django 4.0.2 on 2022-02-22 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='is_delete',
            field=models.BooleanField(db_index=True, default=False, editable=False),
        ),
        migrations.AddField(
            model_name='discount',
            name='name',
            field=models.CharField(default='spring', help_text='A name for discount.', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offcode',
            name='is_delete',
            field=models.BooleanField(db_index=True, default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='discount',
            name='amount',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='offcode',
            name='amount',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='offcode',
            name='code',
            field=models.CharField(help_text='Code that validates the discount.', max_length=30),
        ),
    ]
