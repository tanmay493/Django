from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def home(req):
    # data={"name":"tom",'''age''':True,'qual':False,'x':None}
    # return JsonResponse(data)
  
    # data=10
    # data='python'
    # data=['python']
    # data=('''python''' )
    # data={'python'} #set:-(unordered datatype ko support nahi karta)
 
    return JsonResponse(data,safe=False) # safe=false kyonki bina dictionary format show karne ke liye