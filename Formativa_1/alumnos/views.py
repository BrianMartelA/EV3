from django.shortcuts import redirect, render
from .forms import SignUpForm
from .models import cliente,Registro_cliente
from django.contrib.auth import authenticate, login
from django.contrib import messages


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
    data ={
        'form' : SignUpForm()
    }
    if request.method=="POST":
        formulario= SignUpForm(data=request.POST)
        if formulario.is_valid():

            user=formulario.save()
            Registro_cliente.objects.create(user=user)

            user=authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect('index')
        data["form"] = formulario
    return render(request, 'alumnos/registro.html',data)