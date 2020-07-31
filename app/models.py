from django.db import models
from rest_framework import serializers


class Emp(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()


class MyEmp(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
