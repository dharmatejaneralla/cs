# Generated by Django 3.0.6 on 2020-07-30 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivereddetails', '0005_auto_20200730_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recieveddetails',
            name='pcs',
        ),
        migrations.RemoveField(
            model_name='recieveddetails',
            name='wt',
        ),
    ]