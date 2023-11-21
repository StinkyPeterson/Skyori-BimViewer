from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator

# Create your models here.


class User(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    token = models.CharField(max_length=20)

    def __str__(self):
        return self.login

class Record(models.Model):
    id_record = models.AutoField(primary_key=True)
    date_record = models.DateField()
    login = models.ForeignKey('User', on_delete=models.CASCADE)

class Indicator(models.Model):
    id_indicator = models.AutoField(primary_key=True)
    indicator_name = models.CharField(max_length=100)

class ListIndicators(models.Model):
    id_indicator = models.ForeignKey('Indicator', on_delete=models.CASCADE)
    id_record = models.ForeignKey('Record', on_delete=models.CASCADE)
    value = models.FloatField()

class IFC(models.Model):
    id_ifc = models.AutoField(primary_key=True)
    id_record = models.ForeignKey('Record', on_delete=models.CASCADE)
    date_ifc = models.DateField()
    path = models.CharField(max_length=100)

    def __str__(self):
        return self.path