# Generated by Django 3.0.6 on 2020-07-10 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0003_auto_20200710_1921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='email',
            new_name='email2',
        ),
    ]