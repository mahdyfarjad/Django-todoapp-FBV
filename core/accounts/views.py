from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')        

    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/todo/')
    
    context = {
        'form': UserCreationForm,
        'user': request.user,
    }
    return render(request, 'accounts/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('/accounts/login/')