from django.shortcuts import render,HttpResponse, redirect
from NST.models import Content
from NST.models import Style

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from NST.forms import ContentForm
from NST.forms import StyleForm

from django.core.files import File
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView


# Create your views here.
def index(request):
    return render(request, 'index.html')

def content(request):
    data=Content.objects.all()
    context = {'display':data}
    return render(request, 'content.html', context)

def style(request):
    data=Style.objects.all()
    context = {'display':data}
    return render(request, 'style.html', context)

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def customize(request):
    return render(request, 'customize.html')


def contentfunc(request):
    if request.method == 'POST' or request.FILES == 'file':
        form = ContentForm(request.POST, request.FILES) 
        
        if form.is_valid(): 
            form.save() 
            return redirect('/')
            
    else: 
        form = ContentForm() 
    return render(request, 'NST/index.html',{'form':form}) 

def stylefunc(request):
    if request.method == 'POST' or request.FILES == 'file':
        form = StyleForm(request.POST, request.FILES) 
        
        if form.is_valid(): 
            form.save() 
            return redirect('/')
            
    else: 
        form = StyleForm() 
    return render(request, 'NST/index.html',{'form':form}) 

