from django.db import models

# Create your models here.
class Department(models.Model):
   d_name=models.CharField(max_length=20,unique=True)
   d_dis=models.CharField(max_length=200)
   def __str__(self):
      return self.d_name+","+self.d_dis
   
class Student(models.Model):
    Stu_name=models.CharField(max_length=40)
    Stu_email=models.EmailField(unique=True)
    Stu_contact=models.IntegerField()
    Stu_city=models.CharField(max_length=30)
    

    def __str__(self):
     return self.Stu_name+","+self.Stu_email+","+str(self.Stu_contact)+","+self.Stu_city

class University_Roll(models.Model):
    roll_no=models.CharField(max_length=30,unique=True)
    alloted_date=models.DateField()
    created_by=models.CharField(max_length=30)
    Student_name=models.OneToOneField(Student,on_delete=models.CASCADE) # isme likha hai Student 
                                        # class yadi delete ho gayi yoh University_Roll class
    Stu_dept=models.ForeignKey(Department,on_delete=models.CASCADE)                                    # bhi delete hogi(CASCADE)
    def __str__(self):
     return str(self.roll_no)+','+str(self. alloted_date)+','+self.created_by

class Books(models.Model):
   book_name=models.CharField(max_length=50)
   book_writer=models.CharField(max_length=50)
   book_sub=models.CharField(max_length=50)
   book_price=models.CharField(max_length=50)
   stu_roll=models.ManyToManyField(University_Roll)

   def __str__(self):
      return self.book_name

