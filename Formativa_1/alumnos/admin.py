from django.contrib import admin
from .models import cliente,Registro_cliente
from .models import Categoria, Articulo,detalle_boleta,Boleta
# Register your models here.
admin.site.register(cliente)
admin.site.register(Registro_cliente)
admin.site.register(Categoria)
admin.site.register(Articulo)
admin.site.register(detalle_boleta)
admin.site.register(Boleta)