# Generated by Django 3.0.6 on 2020-08-02 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivereddetails', '0010_auto_20200801_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recieveddetails',
            name='consignmentnumber',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]
