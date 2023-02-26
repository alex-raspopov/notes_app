from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello from Notes app.")


def homepage(request):
    return render(request, 'homepage.html')
