from django.shortcuts import render
from .forms import registroForm
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    context ={}
    return render(request,'alumnos/index.html',context)

def galeria(request):
    context ={}
    return render(request,'alumnos/Galeria.html',context)
def contacto(request):
    context= {}
    return render(request,'alumnos/contacto.html',context)

def quienes_somos(request):
    context = {}
    return render(request,'alumnos/Quienes_somos.html',context)

def boulder(request):
    context = {}
    return render(request,'alumnos/Boulder.html',context)

def registro(request):
    context = {}
    return render(request,'alumnos/Registro.html',context)

def registro_user(request):
    if request.method == 'post':
        form = registroForm(request.post)
        if form.is_valid():
            form.save()
    else:
        form = registroForm()
        
    return render(request,'registro.html',{"form":form})