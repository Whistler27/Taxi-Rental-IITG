# Generated by Django 3.0.6 on 2020-07-10 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0009_auto_20200710_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='email2',
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='car',
            field=models.CharField(choices=[('Maruti Alto', 'MARUTI ALTO'), ('Swift Dzire', 'SWIFT DZIRE'), ('Carpool', 'CARPOOL'), ('Indica', 'INDICA'), ('Innova', 'INNOVA')], default='Indica', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='destination',
            field=models.CharField(choices=[('Panbazaar', 'PANBAZAAR'), ('Paltanbazaar', 'PALTANBAZAAR'), ('Maligaon', 'MALIGAON'), ('GS Road', 'GS ROAD'), ('Airport', 'AIRPORT'), ('Jalukbari', 'JALUKBARI')], default='Panbazaar', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=11),
        ),
    ]
