# Generated by Django 3.0.6 on 2020-08-02 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recdata', '0005_auto_20200719_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recievedata',
            name='conno',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
