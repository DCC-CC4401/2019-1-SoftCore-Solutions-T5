# -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractUser
from django.db import models

class Account(models.Model):
    nombre = models.CharField(max_length=100)
    appellido= models.CharField(max_length=100)
    correo = models.EmailField(max_length=90)
    clave=models.CharField(max_length=100)
    is_superuser=models.BooleanField()

    def __str__(self):
        return self.nombre
