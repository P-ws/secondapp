from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def introduce (request):
    return render(request, "secondapp/change_contents.html")