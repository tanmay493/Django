from django.shortcuts import render
from django.http import HttpResponse
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
    print('hello')
    print(req.GET)  
    print(req.POST) 
    print(req.FILES) 
    print(req.COOKIES)
    print(req.META)