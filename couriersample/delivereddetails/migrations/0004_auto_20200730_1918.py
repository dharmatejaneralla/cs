# Generated by Django 3.0.6 on 2020-07-30 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivereddetails', '0003_auto_20200730_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recieveddetails',
            name='pcs',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='recieveddetails',
            name='wt',
            field=models.CharField(max_length=20),
        ),
    ]
