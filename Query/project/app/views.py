from django.shortcuts import render
from .models import Student
from django.forms.models import model_to_dict

# def single_query(req):
   #  READ operation
#  data=Student.objects.get(id=2)
#  print(data) 
#  data=Student.objects.latest('Name')
#  data=Student.objects.first()
   # data=Student.objects.last()

   # data=Student.objects.all()

 
#  return render(req,'demo.html',data)  #context must be a dict rather than Student.
   # return render(req,'demo.html',{'data':data})
#  data1=model_to_dict(data)
# --------------------------------------------------------------------------------------------
# def multi_query(req):
  #muti value object
#   data=Student.objects.all()
#   print (data)
#   print(data.values())
#   print(data.values_list())
#   print(list(data.values()))
#   return render(req,'demo.html',{'x':data})
   #  return render(req,'demo.html',data) # context must be dict error

   # solution of error
   # data1=model_to_dict(data)
   # n=data.get('Name')
   
# -------------------------------------------------------------------
# data=Student.objects.filter(Name='anshul') sirf anshul naam ka data laayega
# data=Student.objects.order_by('Name') ascending order
# data=Student.objects.order_by('-Name') # descending order
# data=Student.objects.order_by('Name') [0:2] slicing
# data=Student.objects.order_by('-id') [0] # last object
# data=Student.objects.exclude(Name='anshul') # anshul chhod ke sab object show hoga
# print(data)

# -------------------
# CREATE
# Student.objects.create(Name='gukhjhjk')
#   Student.objects.bulk_create([Student(Name='jerry',Email='j@gmail.com',Age=23,Contact=12233445),Student(Name='rock',Email='ro@gmail.com',Age=34,Contact=9876543)])
#  Student.objects.get_or_create(Name='jaguar')
# ----------------------------------------
#   UPDATE

# def new_change(req):
#    data=Student.objects.filter(id=2).update(Contact=6789)
# ---------------------------------------------
#   DELETE

def delete(req):
   data=Student.objects.filter(id=3).delete
   