from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField()
    Email=models.EmailField()
    Contact=models.IntegerField(null=True)
    Gender=models.CharField(null=True)
    Courses=models.CharField(null=True)
    Qualification=models.CharField(null=True)
    Resume=models.FileField(null=True,upload_to='file/')
    Profile_Pic=models.ImageField(null=True,upload_to='images/')
    DOB=models.DateField(null=True)
    Registered_date_time=models.DateTimeField(null=True)
    Registered_time=models.TimeField(null=True)
    Password=models.CharField(null=True)
    Confirm_Password=models.CharField(null=True)



