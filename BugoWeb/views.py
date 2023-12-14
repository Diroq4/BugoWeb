from django.http import HttpResponse
from django.shortcuts import render
from BugoWeb.models import User

# Create your views here.
def register_company(request):
    user = User(name="Diego", phone=3311497650)
    user.save()
    return HttpResponse(f"New user register: {user.name}")