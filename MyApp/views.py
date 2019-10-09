from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'paginaRevenge.html',{})

def otra(request):
    return render(request, 'otra.html',{})
