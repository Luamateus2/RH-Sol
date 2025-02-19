from django.shortcuts  import render,redirect
from django.contrib import messages
from django.db import IntegrityError 
from ..models import Usuario,Funcionario, Setor

def home(request):
    return render(request,'rh/index.html')

def login(request):
     return render(request,'rh/login.html')

def  signup(request):
     return render(request,'rh/signup.html')

