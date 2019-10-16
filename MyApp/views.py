from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

def index(request):
  coco=User.objects.get(username='rosendo')
  return render(request, 'home.html', {'usuario':coco})
