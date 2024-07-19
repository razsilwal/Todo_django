from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    status= models.CharField(max_length=10, null=True) 

