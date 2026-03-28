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

def home(req):

    return render(req,'home.html')