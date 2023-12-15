from django.urls import path
from AppBugo.views import crear_distribuidor, show_html, mostrar_distribuidores

urlpatterns = [
    path('agregar_distribuidor/', crear_distribuidor),
    path('show/', show_html),
    path('distribuidores/', mostrar_distribuidores),

]
