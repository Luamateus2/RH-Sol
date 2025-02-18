from django.shortcuts  import render,redirect
from ..models import Usuario,Funcionario, Setor

def home(request):
    return render(request,'rh/index.html')

def login(request):
     return render(request,'rh/login.html')

def  signup(request):
     return render(request,'rh/signup.html')

def cadastar_funcionario(request):
    if request.method =='POST':
            nome = request.POST.get('nome')
            cpf = request.POST.get('cpf')
            rg = request.POST.get('rg')
            data_nascimento = request.POST.get('dt_nascimento')
            ctps = request.POST.get('ctps')
    return render(request,'rh/index.html')            