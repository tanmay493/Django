from .models import *
from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.
def landing(req):
    return render(req,'landing.html')

def add_student(req):
    if req.method=='POST':
        n = req.POST.get('name')
        e = req.POST.get('email')
        c = req.POST.get('contact')
        ci = req.POST.get('city')
        student = Student.objects.filter(Stu_email = e)
        if student:
            messages.error(req,"Student already exist")
            return redirect('add_student')
        else:
            new_student=Student.objects.create(
                 Stu_name=n,
                 Stu_email=e,
                 Stu_contact=c,
                 Stu_city=ci
                 

            )
            new_student.save()
            messages.success(req,"student added successfully")
            return redirect('add_student')

    return render(req,'add_student.html')


def add_roll(req):
    students = Student.objects.all()
    if req.method=='POST':
        r=req.POST.get('roll_no')
        d=req.POST.get('alloted_date')
        c=req.POST.get('created_by')
        student_id=req.POST.get('Student_name')
        print(student_id)
        students_roll= University_Roll.objects.filter(roll_no=r)
        if students_roll:
            messages.error(req,"rollno already exist")
            return redirect('add_roll')
        else:
            student_obj=Student.objects.get(id=student_id)
            print(student_obj)
            new_roll=University_Roll.objects.create(
                roll_no=r,
                alloted_date=d,
                created_by=c,
                Student_name=student_obj
            )
            new_roll.save()
            
            messages.success(req,"roll_no assigned successfully")
            return redirect('add_roll')
    return render(req,'add_roll.html',{'students':students})

