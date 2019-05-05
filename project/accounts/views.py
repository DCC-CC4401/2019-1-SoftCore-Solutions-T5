# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.shortcuts import render,redirect

# Create your views here.
def signup_view(request):
    form = UserCreationForm()
    return render(request,'accounts/signup.html', {'form':form})

def login_view(request):
    form = AuthenticationForm()
    return render(request,'accounts/login.html', {'form':form})
