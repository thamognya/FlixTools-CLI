from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def general(request):
    return HttpResponse("Hello world")

def name(request, animeName):
    return HttpResponse(animeName)