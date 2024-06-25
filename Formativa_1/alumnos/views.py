from django.shortcuts import redirect, render
from .forms import SignUpForm, UserProfileForm
from .models import cliente,Registro_cliente
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required



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
            group = Group.objects.get(name='cliente')
            user.groups.add(group)

            user=authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect('index')
        data["form"] = formulario
    return render(request, 'alumnos/registro.html',data)



@login_required
def perfil(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'tu contraseña se ha actualizado correctamente')
            return redirect('perfil')
    else:
            form = UserProfileForm(instance=request.user)
    return render(request, 'alumnos/perfil.html',{'form':form})
            