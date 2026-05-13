from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    contact=models.IntegerField()
    department=models.CharField(max_length=50)
    emp_code=models.CharField(max_length=50)
    password=models.CharField(max_length=50)