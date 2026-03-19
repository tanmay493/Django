from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(req):
    return HttpResponse('welcome to django landing page')

def dynamic_int(req,x):
    return HttpResponse(f'my no is {x}')

def dynamic_str(req,x):
    return HttpResponse(f'my name is {x}')

def dynamic_slug(req,x):
    return HttpResponse(f'hello {x}')