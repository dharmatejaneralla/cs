# Generated by Django 3.0.6 on 2020-08-01 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivereddetails', '0009_auto_20200801_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recieveddetails',
            name='consignmentnumber',
            field=models.CharField(max_length=30, null=True),
        ),
    ]