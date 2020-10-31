from django.contrib import admin
from django.urls import path, include

from .views import index, galeria, ubicacion, formulario_insumos, formulario_registro ,mision_vision ,login, cerrar, lista_insumos, eliminar_insumo,buscar,modificar

urlpatterns = [
    
    path('',index,name='INDEX'),
    path('galeria/',galeria,name='GALERIA'),
    path('ubicacion/',ubicacion,name='UBICACION'),
    path('formulario_insumos/',formulario_insumos,name='FORMULARIOINSUMOS'),
    path('formulario_registro/',formulario_registro,name='FORMULARIOREGISTRO'),
    path('mision_vision/',mision_vision,name='MISIONVISION'),
    path('login/',login,name='LOGIN'),
    path('logout_sesion/',cerrar, name='LOGOUT'),
    path('lista_insumos/',lista_insumos,name='LISTAI'),
    path('eliminar_in/<id>/',eliminar_insumo,name='ELIMINARI'),
    path('buscar/<id>/',buscar,name='BUSCAR'),
    path('modificar/',modificar,name='MODIFICAR'),
]
