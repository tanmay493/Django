from django.shortcuts import render ,redirect
from django.contrib import messages

# Create your views here.
def landing(req):
    return render(req,'landing.html')

def my_render(req):
    messages.success(req,'data creation done')
    messages.info(req,'data is here')
    return render(req,'landing.html')
   
def my_redirect(req):
    messages.success(req,'data successfully stored')
    return redirect('landing')
