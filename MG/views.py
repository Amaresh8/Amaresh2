from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Python(request):
    return HttpResponse("INTERESTING IT SEEMS GOOD")

def Python2(request):
    return HttpResponse("<h1>LINK PYTHON WITH DJANGO</h1>")