# Generated by Django 2.0 on 2018-01-03 14:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AddressBook', '0005_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='zipcode',
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message="Zip code must be entered in the format: '666666'. Exactly 6 digits allowed.", regex='^\\d{6}$')]),
        ),
    ]
