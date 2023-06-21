from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

def index(response, id):
  ls = ToDoList.objects.get(id=id)
  return render(response, "app_name/base.html", {"name":ls.name})

def home(response):
  return render(response, "app_name/home.html", {"name":"Name"})