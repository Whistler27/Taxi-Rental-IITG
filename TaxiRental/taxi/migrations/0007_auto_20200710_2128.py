# Generated by Django 3.0.6 on 2020-07-10 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0006_auto_20200710_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='email2',
            field=models.CharField(max_length=111, null=True),
        ),
    ]
