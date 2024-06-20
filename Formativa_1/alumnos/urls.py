from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('galeria',views.galeria,name='galeria'),
    path('contacto',views.contacto,name='contacto'),
    path('quienes_somos',views.quienes_somos,name='quienes_somos'),
    path('boulder',views.boulder,name='boulder'),
    path('registro',views.registro,name='registro'),
    path('perfil',views.perfil, name='perfil')
]
