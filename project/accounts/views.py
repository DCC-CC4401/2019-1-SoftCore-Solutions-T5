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
        form=AccountForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido= form.cleaned_data['appellido']
            correo = form.cleaned_data['correo']
            clave = form.cleaned_data['clave']
            account = Account.objects.create(nombre = nombre, appellido = apellido,
                                          correo = correo,
                                          clave = clave, is_superuser = False)
            account.save()
            nickname = nombre + apellido
            user = User.objects.create_user(username=nickname, email=correo, password=clave)
            user.save()
            return redirect('/accounts/signup')
        else:
            return render(request,'accounts/signup.html', {'form':form, 'accounts':accounts})
    else:
        form = AccountForm()
    accounts = Account.objects.all()
    return render(request,'accounts/signup.html', {'form':form, 'accounts':accounts})

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
