# Generated by Django 3.0.6 on 2020-07-23 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drs', '0004_auto_20200723_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drsdata',
            name='conno',
            field=models.CharField(max_length=15),
        ),
    ]
