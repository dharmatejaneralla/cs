# Generated by Django 3.0.8 on 2020-07-19 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recdata', '0004_auto_20200718_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recievedata',
            name='date',
            field=models.CharField(max_length=15),
        ),
    ]
