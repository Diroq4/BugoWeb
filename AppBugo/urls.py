from django.urls import path
from AppBugo.views import crear_distribuidor, show_html, mostrar_distribuidores, busqueda_distribuidor, contactanos

urlpatterns = [
    path('agregar_distribuidor/', crear_distribuidor),
    path('show/', show_html),
    path('distribuidores/', mostrar_distribuidores),
    path('buscar_distribuidor/', busqueda_distribuidor),
    path('contactar/', contactanos),

]
