from django.shortcuts import render,redirect

# Create your views here.
def my_redirect1(req):

    return redirect('first')  #for internal redirect

def first(req):
    return render(req,'landing.html')  
# ----------------------------------------
# def my_redirect1(req):

#      return redirect('https://www.google.com/')  # //for external css
# -------------------------------------------------------------

def my_redirect2(req):
    # return redirect('second',1,2,3)           # *args (positional argument)
    
    data=[1,2,3]
    # data=(1,2,3)
    return redirect ('second',*data)
    

def second(req,x,y,z):
    data={'p':x,'q':y,'r':z}
    return render(req,'second.html',data) # data is var. which is called context
                                         # which should be in dictionary format
# -----------------------------------------------------------------------------
def my_redirect3(req):
    # return redirect('third',x=10,y=20,z=30)
    data={'x':'tom','y':23,'z':'btech'}
    return redirect('third',**data) #   *data  single star(*) diya toh sirf key print
                                    #karega , agar **data double star(**) diya toh
                                    #key ki value print karega

def third(req,x,y,z):
    data={'p':x,'q':y,'r':z}
    return render(req,'third.html',data)


