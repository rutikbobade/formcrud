from multiprocessing import context
from re import template
import re
from django.shortcuts import redirect, render

from formcrudapp.forms import crudforms
from formcrudapp.models import crud

# Create your views here.

def registration(request):
    if request.method=='POST':
        form=crudforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('table')
    form=crudforms()
    template_name='index.html'
    context={'form':form}
    return render(request,template_name,context)

def Table(request):
    obj=crud.objects.all()
    context={'obj':obj}
    template_name='table.html'
    return render(request,template_name,context)

def delete(request,id):
    obj=crud.objects.get(id=id)
    obj.delete()
    return redirect('table')

def update(request,id):
    obj=crud.objects.get(id=id)

    if request.method=='POST':
        form=crudforms(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('table')
    form=crudforms(instance=obj)
    template_name='update.html'
    context={'form':form}
    return render(request,template_name,context)        




