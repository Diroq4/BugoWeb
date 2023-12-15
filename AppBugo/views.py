from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppBugo.forms import DistribuidorForm
from AppBugo.models import Distribuidor

def mostrar_distribuidores(request):
    distribuidores = Distribuidor.objects.all()
    contexto = {"distribuidores": distribuidores, "nombre": "Diego"}
    return render(request,"AppBugo/distribuidores.html", contexto)

# def crear_distribuidor(request):
#     distribuidor = Distribuidor(nombre="Diego", telefono=456)
#     distribuidor.save()
#     return redirect("/app/distribuidores/")

def show_html(request):
    distribuidor = Distribuidor.objects.first()
    contexto = {"distribuidor": distribuidor, "nombre": "Diego"}
    return render(request, "index.html", contexto)

def crear_distribuidor(request):
    if request.method == "POST":
        # Crear distribuidor
        distribuidor_formulario = DistribuidorForm(request.POST)
        if distribuidor_formulario.is_valid:
            informacion = distribuidor_formulario.cleaned_data

            distribuidor_crear = Distribuidor(nombre = informacion.nombre, telefono = informacion.telefono, email = informacion.email)
            distribuidor_crear.save()
            return redirect("/app/distribuidores/")

    distribuidor_formulario = DistribuidorForm()
    contexto = {
        "form": distribuidor_formulario
    }
    return render(request, "AppBugo/crear_distribuidor.html", contexto)