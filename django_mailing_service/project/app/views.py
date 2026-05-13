from django.shortcuts import render,redirect
from .models import *
from django.core.mail import send_mail
from django.contrib import messages
import random



# Create your views here.
def landing(req):
    if req.method=='POST':
        n=req.POST.get('name')
        e=req.POST.get('email')
        c=req.POST.get('contact')
        d=req.POST.get('department')
        emp=req.POST.get('emp_code')
        p=req.POST.get('password')

        Unique=Employee.objects.filter(email=e)
        if Unique:
            messages.error(req,"you are already registered go to login page")
            return redirect('login')
        else:
    
            send_mail(
        "company id_password", #subject
        f'your email id is {e} and password is {p}', # main body
        "tanmaylanjewar24874@gmail.com", # from sender email id
        [e],# to reciever email id [e]=>because humne humne dynamic banaya hai
        fail_silently=False,
    )
            Employee.objects.create(name=n,email=e,contact=c,department=d,emp_code=emp,password=p)    

    return render(req,'landing.html')

def login(req):
    
    if req.method=='POST':
       e=req.POST.get('email')
       
       Emp=Employee.objects.filter(email=e)
       if Emp.exists():
         return render(req,"login.html")
         
       else:
         messages.error("first register yourself in registration")
         return redirect('landing')
    return render(req,'login.html')

def forget_password(req):
    if req.method=='POST':
        e=req.POST.get('email')
        u_email=Employee.objects.filter(email=e)
        if not u_email:
            messages.error(req,"email id is not registered")
            return redirect('forget_password')
        else:
            otp=random.randint(1111,9999)
            req.session['email']=e
            req.session['otp']=otp
            send_mail("mail from django server",f'your otp is {otp}',"tanmaylanjewar24874@gmail.com",[e])
            messages.success(req,"otp has been sent to your email id")
            return redirect('otp_verify')
    return render(req,'forget_password.html')

def otp_verify(req):
 if 'email' in req.session and 'otp' in req.session:
     e=req.session.get('email')
     return render(req,'otp_verify.html',{'email':e})
 else:
     return redirect('login')
 
def verify(req):
    if 'email' in req.session and 'otp' in req.session:
        if req.method=='POST':
            sess_e=req.session.get('email')
            sess_o=req.session.get('otp')

            user_e=req.POST.get('email')
            user_o=int(req.POST.get('otp'))
            print(sess_e,sess_o,user_e,user_o)
            print(type(sess_o),type(user_o))
            if sess_e==user_e and sess_o==user_o:
                return render(req,'reset.html',{'email':user_e})
            else:
                messages.error(req,"email and otp are not matched")
                return render(req,'otp_verify.html')
    else:
        return redirect('login')

def reset(req):
    if 'email' in req.session and 'otp' in req.session:
        if req.method=='POST':
            e=req.POST.get('email')
            np=req.POST.get('new_password')
            cp=req.POST.get('confirm_password')

            if np!=cp:
                return redirect('reset')
            else:
                old_userdata=Employee.objects.get(email=e)
                old_userdata.password=np
                old_userdata.save()
                return redirect('login')



    return render(req,'reset.html')