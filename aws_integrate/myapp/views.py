from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def read(request):
    return HttpResponse('Hello Python World!')
    

