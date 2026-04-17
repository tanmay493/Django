from django.shortcuts import render

# Create your views here.
def set_data(req):
    if req.method=='POST':
        n=req.POST.get('name')
        e=req.POST.get('email')
        p=req.POST.get('password')
        req.session['name']=n
        req.session['email']=e
        req.session['password']=p
        return render(req,'landing.html',{'msg':'data set successfully'})
    return render(req,'landing.html',{'set_data':True})

def landing(req):
    return render(req,'landing.html')

def get_data(req):
    if 'name' in req.session and 'email' in req.session and 'password' in req.session:
        n=req.session.get('name')
        e=req.session.get('email')
        p=req.session.get('password')
        data={'name':n,'email':e,'password':p}
        return render(req,'landing.html',{'data':data})
    else:
        msg='data may be empty or deleted'
        return render(req,'landing.html',{'msg':msg})

def delete_data(req):
     if 'name' in req.session and 'email' in req.session and 'password' in req.session:
        #  del req.session['name']
        #  del req.session['email']
        #  del req.session['password']
        req.session.flush() # for data deletion from server side
        return render(req,'landing.html',{'msg':'data deleted'})
     
     else:
         msg='first fill the data which you want to delete'
         return render(req,'landing.html',{'msg':msg})