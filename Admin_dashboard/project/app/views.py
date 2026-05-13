from django.shortcuts import render,redirect
from django.views.decorators.cache import never_cache


# Create your views here.
def landing(req):
    return render(req,'landing.html')

def admin_dashboard(req):
    return redirect('login')

def emp_dashboard(req):
    return redirect('login')

def login(req):
    return render (req,'login.html')

def login_data(req):
    if req.method=='POST':
      e=req.POST.get('email')
      p=req.POST.get('password')
      
      if e=='admin@gmail.com' and p=='admin':
          return render (req,'admin_dashboard.html')
      else:
        
          return render(req,'emp_dashboard.html')
          
      
        
    return render(req,'login.html')

@never_cache
def logout(req):
    return redirect('login')

def add_employee(req):
    return   

def add_department(req):
    return  

def all_query(req):
    return 

