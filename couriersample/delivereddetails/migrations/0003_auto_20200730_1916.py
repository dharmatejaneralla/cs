# Generated by Django 3.0.6 on 2020-07-30 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivereddetails', '0002_auto_20200730_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recieveddetails',
            name='wt',
            field=models.CharField(max_length=10),
        ),
    ]
