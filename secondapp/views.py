from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def introduce (request):
    return HttpResponse("Hi. my name is woosung")