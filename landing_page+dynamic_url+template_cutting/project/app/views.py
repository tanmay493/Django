from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from django.views.decorators.cache import never_cache

# Create your views here.

def landing(req):
    # return HttpResponse('welcome to django landing page')
    return render(req,'landing(base).html')

def dynamic_int(req,x):
    return HttpResponse(f'my no is {x}')

def dynamic_str(req,x):
    return HttpResponse(f'my name is {x}')

def dynamic_slug(req,x):
    return HttpResponse(f'hello {x}')


def login(req):

    return render(req,'login.html')


def register(req):

    return render(req,'register.html')



def contact(req):

    return render(req,'contact.html')

def about(req):
    return render(req,'about.html')

def home(req):

    return render(req,'home.html')

def feature(req):
    data=[{'name':'tom', 'age':23},{'name':'john', 'age':27},{'name':'rock', 'age':45}]  
    # data={'name':'tom', 'age':23}
    return render (req,'feature.html',{'xyz':data})  

def reg_data(req):
    # print('hello')
    # print(req.GET)  
    # print(req.POST) 
    # print(req.FILES) 
    # print(req.COOKIES)
    # print(req.META)

    if req.method=='POST':
        n=req.POST.get('name')
        e=req.POST.get('email')
        c=req.POST.get('contact')
        g=req.POST.get('gender')
        co=req.POST.getlist('courses')
        q=req.POST.get('qualification')
        r=req.FILES.get('resume')
        pic=req.FILES.get('profile_pic')
        d=req.POST.get('dob')
        rdt=req.POST.get('registered_date_time')
        rt=req.POST.get('registered_time')
        p=req.POST.get('password')
        cp=req.POST.get('confirm_password')
        print(p,r)
        user=Student.objects.filter(Email=e)
        if user:
            msg='Email already exist'
            return render(req,'register.html',{'msg': msg})
        else:
            if p==cp:
                Student.objects.create(Name=n,Email=e,Contact=c,Gender=g,Courses=co,Qualification=q,Resume=r,Password=p,Confirm_Password=cp,Registered_date_time=rdt,Registered_time=rt,DOB=d,Profile_Pic=pic)    
                msg="registration successful"
                return render(req,'login.html',{'msg1':msg})
            else:
                msg='password & confirm_password does not match'    
                return render(req,'register.html',{'msg2':msg,'n':n,'e':e})
@never_cache
def login_data(req):
    if req.method=='POST':
        e=req.POST.get('email')  
        p=req.POST.get('password')
        print(e,p,sep=',')
        user=Student.objects.filter(Email=e)
        if user:
            user_data=Student.objects.get(Email=e)
            save_pass=user_data.Password
            if p==save_pass:
                req.session['user_id']=user_data.id
                return redirect('dashboard')
                
            else:
                msg="email and password not matched"
                return render(req,'login.html',{'msg1':msg,'email':e})
        else:
            msg='email id not present in db'
            return render(req,'register.html',{'msg':msg})   

@never_cache
def dashboard(req):
    # print(x) 
    if 'user_id' in req.session:  
        user_id=req.session.get('user_id')
        user_data=Student.objects.get(id=user_id)
        data={'name':user_data.Name,'email':user_data.Email,'password':user_data.Password}
        return render(req,'dashboard.html',{'data':data})
    else:
        return redirect('login')

@never_cache
def logout(req):
    if 'user_id' in req.session:
        req.session.flush()
        return redirect('login')
    else:
        return redirect('login')