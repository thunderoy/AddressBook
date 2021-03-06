# Generated by Django 2.0 on 2018-01-08 09:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AddressBook', '0007_auto_20180103_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='zip_code',
            field=models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message="Zip code must be entered in the format: '666666'. Exactly 6 digits allowed.", regex='^\\d{6}$')]),
        ),
    ]
