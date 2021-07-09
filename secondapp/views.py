from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def introduce (request):
    if request.method =='POST':
        return render(request, "secondapp/change_contents.html",
                      context={'text': 'POST METHOD!'})
    else:
        return render(request, "secondapp/change_contents.html",
                      context={'text': 'POST METHOD!'})