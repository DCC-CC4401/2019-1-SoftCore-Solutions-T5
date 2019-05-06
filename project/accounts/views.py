# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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
    return render(request,'accounts/signup.html', {'form':form})

def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('/home')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html', {'form':form})
