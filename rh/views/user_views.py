from django.contrib.auth import get_user_model
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from ..models import  User


def add_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'rh/signup.html')

        User = get_user_model()

        if User.objects.filter(email=email).exists():
            messages.error(request, "This email is already in use.")
            return render(request, 'rh/signup.html')

        try:
            new_user = User.objects.create_user(
                email=email, name=name, password=password)
            messages.success(
                request, "User successfully created! Log in to continue.")
            return render(request, 'rh/login.html')
        except Exception as e:
            messages.error(
                request, "An error occurred while creating the user. Please try again.")
            return render(request, 'rh/signup.html')
    else:
        return render(request, 'rh/signup.html')




def authenticate_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            print('autenticado')
            return redirect('home')
        else:
            messages.error(request, "Email ou senha incorreto.")
            return render(request, 'rh/login.html')

    return render(request, 'rh/login.html')

