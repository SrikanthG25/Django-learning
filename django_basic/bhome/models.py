from django.db import models
from django.http import HttpResponse

# Create your models here.
class data(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Address=models.CharField(max_length=50)
    Contact=models.BigIntegerField()
    Mail=models.CharField(max_length=50)
