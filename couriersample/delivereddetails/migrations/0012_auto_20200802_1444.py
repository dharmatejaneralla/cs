# Generated by Django 3.0.6 on 2020-08-02 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivereddetails', '0011_auto_20200802_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recieveddetails',
            name='consignmentnumber',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
