# Generated by Django 3.0.6 on 2020-07-10 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0005_auto_20200710_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='car',
            field=models.CharField(max_length=111, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='destination',
            field=models.CharField(max_length=111, null=True),
        ),
    ]
