# Generated by Django 2.2 on 2020-06-26 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disaster', '0002_severe_pollution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='severe_pollution',
            name='CO_off',
            field=models.BooleanField(),
        ),
    ]
