from django.shortcuts import render

def home(request):
    return render(request, 'infoDir/home.html') 

def about(request):
    return render(request, 'infoDir/about.html')
