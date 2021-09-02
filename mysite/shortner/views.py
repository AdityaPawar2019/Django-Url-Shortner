from django.shortcuts import render

from django.shortcuts import HttpResponse

def HelloWorld(request):
    return HttpResponse("Helllo World")