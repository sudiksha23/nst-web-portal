from django.shortcuts import render,HttpResponse, redirect
from NST.models import NstImages
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from NST.forms import NstImagesForm
from django.core.files import File
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def content(request):
    data=NstImages.objects.all()
    context = {'display':data}
    return render(request, 'content.html', context)

def style(request):
    data=NstImages.objects.all()
    context = {'display':data}
    return render(request, 'style.html', context)

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def customize(request):
    return render(request, 'customize.html')


def nstimages(request):
    if request.method == 'POST' or request.FILES == 'file':
        form = NstImagesForm(request.POST, request.FILES) 
        
        if form.is_valid(): 
            form.save() 
            return redirect('/')
            
    else: 
        form = NstImagesForm() 
    return render(request, 'NST/index.html',{'form':form}) 

