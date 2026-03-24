from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(req):
    # register='<h1>hi</h1>'
   
    # data={'x':10,'y':20,'z':30}
    data='{"x":10,"y":20,"z":30}' #json ka datatype


    # return HttpResponse(content='hello',content_type=None)
   
    # return HttpResponse(content=register) #dono register ek hi hai likhne ka tarika diff. hai
    # return HttpResponse(content=register,content_type='text/html')
   
    # return HttpResponse(data)
    return HttpResponse(data,content_type='application/json')