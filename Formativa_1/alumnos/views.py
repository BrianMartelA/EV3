from django.shortcuts import redirect, render
from .forms import SignUpForm
from .models import cliente,Registro_cliente
from .models import Articulo, Boleta, detalle_boleta
from django.contrib.auth import authenticate, login
from django.contrib import messages
from alumnos.compra import Carrito


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

def tienda(request):
    articulos = Articulo.objects.all()
    datos={
        'articulos':articulos
    }
    return render(request, 'alumnos/tienda.html', datos)


def agregar_producto(request,id):
    carrito_compra= Carrito(request)
    articulo = Articulo.objects.get(codigo=id)
    carrito_compra.agregar(articulo=articulo)
    return redirect('tienda')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    articulo = Articulo.objects.get(codigo=id)
    carrito_compra.eliminar(articulo=articulo)
    return redirect('tienda')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    articulo = Articulo.objects.get(codigo=id)
    carrito_compra.restar(articulo=articulo)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('tienda')    


def generarBoleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Articulo.objects.get(codigo = value['articulo_id'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            detalle.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'alumnos/detallecarrito.html',datos)