# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

# Create your views here.
def signup_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/signup')
        else:
            return render(request,'accounts/signup.html', {'form':form})
    else:
        form = UserCreationForm()
    accounts = User.objects.filter(is_superuser=False)
    return render(request,'accounts/signup.html', {'form':form}, {'accounts':accounts})

def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('/home')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html', {'form':form})


def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('.')
