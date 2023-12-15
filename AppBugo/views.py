from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppBugo.models import Distribuidor

def mostrar_distribuidores(request):
    distribuidores = Distribuidor.objects.all()
    contexto = {"distribuidores": distribuidores, "nombre": "Diego"}
    return render(request,"AppBugo/distribuidores.html", contexto)

def crear_distribuidor(request):
    distribuidor = Distribuidor(nombre="Diego", telefono=456)
    distribuidor.save()
    return redirect("/app/distribuidores/")

def show_html(request):
    distribuidor = Distribuidor.objects.first()
    contexto = {"distribuidor": distribuidor, "nombre": "Diego"}
    return render(request, "index.html", contexto)

