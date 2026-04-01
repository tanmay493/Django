from django.shortcuts import render

# Create your views here.
def home(req):
    data={'name':'tom','city':'bhopal','p':'this is django class'}
    return render(req,'home.html',data)


def about(req):

    return render(req,'about.html')