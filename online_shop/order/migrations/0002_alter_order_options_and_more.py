# Generated by Django 4.0.2 on 2022-02-22 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_address_options_address_is_delete_and_more'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='discount_code',
            new_name='off_code',
        ),
        migrations.AddField(
            model_name='order',
            name='is_delete',
            field=models.BooleanField(db_index=True, default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='customer.customer'),
        ),
    ]
