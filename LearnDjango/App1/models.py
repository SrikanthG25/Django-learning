from django.db import models

# Create your models here.
class Staffdata(models.Model):
    Name = models.CharField(max_length=20)
    Age = models.IntegerField()
    Position = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=20,decimal_places=5)    
    City = models.CharField(max_length=15)


 