# Generated by Django 3.0.6 on 2020-07-18 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recievedata',
            name='wt',
            field=models.CharField(max_length=5),
        ),
    ]
