# Generated by Django 5.0.7 on 2024-07-27 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STAS', '0007_recruitmentmaster_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitmentmaster',
            name='experience',
            field=models.IntegerField(max_length=10),
        ),
    ]
