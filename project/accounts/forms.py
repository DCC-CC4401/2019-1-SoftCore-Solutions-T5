# -*- coding: utf-8 -*-
from django import forms

class AccountForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    appellido=forms.CharField(max_length=100)
    correo = forms.EmailField(max_length=90)
    clave=forms.CharField(max_length=30)
