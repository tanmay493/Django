from django.shortcuts import render

# Create your views here.
def landing(req):
    # return HttpResponse('welcome to django landing page')
    return render(req,'landing(base).html')
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
    # print(req.GET)  
    print(req.POST) 
    print(req.FILES) 
    # print(req.COOKIES)
    # print(req.META)    
    n = req.POST.get('name')
    e = req.POST.get('email')
    co = req.POST.get('contact_no.')
    p = req.POST.get('password')
    g = req.POST.get('gender')
    c = req.POST.getlist('courses')
    q = req.POST.get('qualification')
    r = req.POST.get('resume')
    rdt = req.POST.get('registered_date_time')
    rt = req.POST.get('registered_time')
    pp=req.FILES.get('profile_pic')
    print(n,e,co,r,q,rt,rdt,p,g,c,pp,sep=',')


