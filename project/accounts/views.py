# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import *
from .models import Account
from .forms import AccountForm

# Create your views here.
def signup_view(request):
    if request.method=='POST':
        nombre = request.POST['nombre']
        apellido= request.POST['apellido']
        correo = request.POST['correo']
        clave = request.POST['clave']
        account = Account.objects.create(nombre = nombre, appellido = apellido,
                                       correo = correo,
                                       clave = clave, is_superuser = False)
        account.save()
        nickname = nombre + apellido
        user = User.objects.create_user(username=nickname, email=correo, password=clave)
        user.save()
        accounts = Account.objects.all()
        return redirect('/accounts/signup', {'accounts': accounts})
    accounts = Account.objects.all()
    return render(request,'accounts/signup.html', {'accounts': accounts})

def login_view(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            username = User.objects.get(email=email).username
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home')
        except User.DoesNotExist:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return render(request,'accounts/login.html')


def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('.')
