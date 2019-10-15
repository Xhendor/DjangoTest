from django.shortcuts import render
from array import *
from django.http import HttpResponse

from .models import Board

def index(request):
    data = Board.objects.all()
    return render(request, 'paginaRevenge.html',{'posts': data})

def otra(request):
    return render(request, 'otra.html',{})
