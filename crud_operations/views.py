from django.shortcuts import render,HttpResponseRedirect
from .models import *
from .forms import *
# Create your views here.

def show(request):
    if request.method=="POST":
        fm=CustomerForms(request.POST)
        if fm.is_valid():
            fm.save()
        fm=CustomerForms()
    else:
        fm=CustomerForms()
    customer_data=Customer.objects.all()
    print(customer_data)
    return render(request,"crud_operations/display.html",{"form":fm,"customer":customer_data})

def update_data(request,id):
    if request.method=='POST':
        obj=Customer.objects.get(pk=id)
        form=CustomerForms(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    else:
        obj=Customer.objects.get(pk=id)
        form=CustomerForms(instance=obj)
    return render(request,"crud_operations/update.html",{"form":form})

# This function for delete
def delete_cust(request,id):
    obj=Customer.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/')
