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





