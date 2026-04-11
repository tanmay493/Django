from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Contact_No=models.IntegerField(max_length=10)
    Password=models.CharField()
    
    def __str__(self):
        return self.Name+' '+self.Email
