
from django.shortcuts import render, HttpResponse
from .models import Pelicula

def home(request):
        return render(request, "infoDir/home.html")
def peli(request):
        return render(request, "infoDir/peli.html")
def about(request):
        return render(request, "infoDir/about.html")
def valoradas(request):
        return render(request,"infoDir/valoradas.html")