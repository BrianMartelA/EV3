from django.urls import path
from alumnos.views import *

urlpatterns = [
    path('index/',index,name='index'),
    path('galeria/',galeria,name='galeria'),
    path('contacto/',contacto,name='contacto'),
    path('quienes_somos/',quienes_somos,name='quienes_somos'),
    path('boulder/',boulder,name='boulder'),
    path('registro/',registro,name='registro'),

    path('tienda/',tienda, name="tienda"),
    path('tienda/',tienda, name="tienda"),
    path('generarBoleta/', generarBoleta,name="generarBoleta"),
    path('agregar/<id>', agregar_producto, name="agregar"),
    path('eliminar/<id>', eliminar_producto, name="eliminar"),
    path('restar/<id>', restar_producto, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
    
]
