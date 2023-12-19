from django.urls import path
from AppBugo.views import show_html, busqueda_distribuidor, contactanos, \
    DistribuidoresList, DistribuidorDetalle, DistribuidorCreacion, DistribuidorActualizacion, DistribuidorEliminar

urlpatterns = [
    # path('agregar_distribuidor/', crear_distribuidor),
    path('show/', show_html),
    # path('distribuidores/', mostrar_distribuidores),
    path('buscar_distribuidor/', busqueda_distribuidor),
    path('contactar/', contactanos),
    path('distribuidores/listar/', DistribuidoresList.as_view(), name="lista"),
    path('distribuidor/<int:pk>', DistribuidorDetalle.as_view(), name="detalle"),
    path('crear/', DistribuidorCreacion.as_view(), name="cursocreate"),
    path('actualizar/<int:pk>', DistribuidorActualizacion.as_view(), name="actualizar"),
    path('eliminar/<int:pk>', DistribuidorEliminar.as_view(), name="eliminar"),

]
