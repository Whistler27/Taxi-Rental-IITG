# Generated by Django 3.0.6 on 2020-07-10 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0002_orders_orderupdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='items_json',
        ),
    ]
