from django.db import models

# Create your models here.
class Delboys(models.Model):
    boyname = models.CharField(max_length=40)

class Area(models.Model):
    areaname = models.CharField(max_length=40)

class DrsData(models.Model):
    date = models.CharField(max_length=15)
    drsno = models.IntegerField
    conno = models.CharField(max_length=15)
    pcs = models.IntegerField()
    wth = models.CharField(max_length=20)
    boy = models.CharField(max_length=30)
    area = models.CharField(max_length=30)

class Dummydrs(models.Model):
    dummydrs = models.IntegerField()