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

        if (n and e and p):
            resp=render(req,'landing_page.html',{'msg':"cookie has been set"})
            resp.set_cookie('name',n)
            resp.set_cookie('email',e)
            resp.set_cookie('password',p)
            return resp
        else:
            return render(req,'landing_page.html',{'msg':'some values are missing','xyz':True})


    return render(req,'landing_page.html',{'xyz':True})

def get_cookie(req):
    if (req.COOKIES.get('name')and req.COOKIES.get('email')and req.COOKIES.get('password')):
        n=req.COOKIES.get('name')
        e=req.COOKIES.get('email')
        c=req.COOKIES.get('password')
        print(req.COOKIES)
        data={'name':n,'email':e,'contact':c}
        return render(req,'landing_page.html',{'data':data})
    else:
        return render(req,'landing_page.html',{'msg':'cookies are empty'})

def delete(req):
    if (req.COOKIES.get('name')and req.COOKIES.get('email')and req.COOKIES.get('contact')):
        response=render(req,'landing_page.html',{'msg':"cookies are deleted"})
        response.delete_cookie('name')
        response.delete_cookie('email')
        response.delete_cookie('contact')
        return response
    else:
         return render(req,'landing_page.html',{'msg':'cookies are empty'})
