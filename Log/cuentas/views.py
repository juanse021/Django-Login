from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from . forms import UserRegistrationForm
# Create your views here.

def login_usuario(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        remeber = request.POST.get('remeber')
        if remeber:
            settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Bad username or password')
    return render(request, 'login.html', {})

def logout_usuario(request):
    logout(request)
    return redirect('cuentas:login')

def registrar_usuario(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username, email=email, password=password)
            messages.success(request, 'Gracias por registrarse {}'.format(user.username))
            return redirect('cuentas:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registrar.html', {'form':form})
