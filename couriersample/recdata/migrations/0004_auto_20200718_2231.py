# Generated by Django 3.0.6 on 2020-07-18 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recdata', '0003_auto_20200718_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recievedata',
            name='mfno',
            field=models.CharField(max_length=12),
        ),
    ]
