from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "hi/index.html")

def brain(request):
    return HttpResponse("Hey brain")

def david(request):
    return HttpResponse("Hey david")

def greet(request, name):
    return render(request, "hi/greet.html",{
        "name": name.capitalize()
    })

