# Generated by Django 3.2.25 on 2024-06-26 18:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STAS', '0003_test_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitmentmaster',
            name='mobile_number',
            field=models.CharField(max_length=13, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(13), django.core.validators.RegexValidator('^\\+91\\d{10}$')]),
        ),
    ]
