from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField(unique=True,max_length=40,)
    Age=models.IntegerField(null=True)
    Contact=models.CharField(max_length=10,unique=True,null=True)
    

    
    def __str__(self):
        return self.Name+'   '+self.Email+'   '+str(self.Age)+'   '+str(self.Contact)
