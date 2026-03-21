from django.shortcuts import render

# Create your views here.
def landing(req):
    data={
        "name":"tom",
        "age":22
    }
    return render(req,'landing.html',data)