from django.http import HttpResponse
from django.shortcuts import render
from BugoWeb.models import User, Distributor


# Create your views here.
def register_company(request):
    user = User(name="Diego", phone=3311497650)
    user.save()
    return HttpResponse(f"New user register: {user.name}")

def show_distributor(request):
    distributor = Distributor.objects.all()
    contexto = {"distributor": distributor}
    return render(request,"BugoWeb/distributor.html", contexto)

def create_distributor(request):
    distributors = Distributor(name="Diego")
    distributors.save()
    contexto = {"distributors": distributors}
    return render(request,"index.html",contexto)

def show_html(request):
    contexto = {}
    return render(request,"index.html", contexto)