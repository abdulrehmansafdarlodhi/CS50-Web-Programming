from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hey")

def brain(request):
    return HttpResponse("Hey brain")

def david(request):
    return HttpResponse("Hey david")

def greet(request, name):
    return HttpResponse(f"As-Salaam-Alaikum {name.capitalize()}!")

