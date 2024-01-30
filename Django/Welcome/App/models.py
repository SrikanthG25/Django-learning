from django.db import models

class Excelmodel(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Description = models.TextField()
