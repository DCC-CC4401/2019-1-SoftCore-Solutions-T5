from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class Account(models.Model):
   user = models.OneToOneField(User, unique=True)
   #other field in that profile
   #other field in that profile
   #other field in that profile
