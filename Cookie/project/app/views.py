from django.shortcuts import render

# Create your views here.
def landing_page(req):
    return render(req,'landing_page.html')

def set(req):
    if req.method=="POST":
        n= req.POST.get('name')
        e= req.POST.get('email')
        p= req.POST.get('password')
        print(n,e,p)
        resp=render(req,'landing_page.html',{'msg':"cookie has been set"})
        resp.set_cookie('name',n)
        resp.set_cookie('email',e)
        resp.set_cookie('password',p)
        return resp


    return render(req,'landing_page.html',{'xyz':True})