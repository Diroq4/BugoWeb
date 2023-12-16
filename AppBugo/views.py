from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppBugo.forms import DistribuidorForm, BusquedaDistribuidorForm, ContactanosForm
from AppBugo.models import Distribuidor, Contacto


def mostrar_distribuidores(request):
    distribuidores = Distribuidor.objects.all()
    contexto = {"distribuidores": distribuidores, "nombre": "Diego", "form": BusquedaDistribuidorForm()}
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
        if distribuidor_formulario.is_valid():
            informacion = distribuidor_formulario.cleaned_data

            distribuidor_crear = Distribuidor (nombre = informacion["nombre"], telefono = informacion["telefono"], email = informacion["email"])
            distribuidor_crear.save()
            return redirect("/app/distribuidores/")

    distribuidor_formulario = DistribuidorForm()
    contexto = {
        "form": distribuidor_formulario
    }
    return render(request, "AppBugo/crear_distribuidor.html", contexto)

def busqueda_distribuidor(request):
    nombre = request.GET["nombre"]
    distribuidores = Distribuidor.objects.filter(nombre__icontains=nombre)
    contexto = {"distribuidores": distribuidores, "nombre": "Diego", "form": BusquedaDistribuidorForm()}
    return render(request,"AppBugo/distribuidores.html", contexto)

def contactanos(request):
    if request.method == "POST":
        # Crear distribuidor
        contacto_formulario = ContactanosForm(request.POST)
        if contacto_formulario.is_valid():
            informacion = contacto_formulario.cleaned_data

            contacto_crear = Contacto (nombre = informacion["nombre"], telefono = informacion["telefono"])
            contacto_formulario.save()
            return "Nos podendremos en contacto!"

    contacto_formulario = ContactanosForm()
    contexto = {
        "form": contacto_formulario
    }
    return render(request, "AppBugo/distribuidores.html", contexto)
