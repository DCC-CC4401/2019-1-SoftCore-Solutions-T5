# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
    CHOICES1 = (("Primavera", "Primavera"),("Otoño", "Otoño"),)
    CHOICES2 = ((1,1),(2, 2),)
    title=models.CharField(max_length=200)
    code=models.CharField(max_length=20)
    semester=models.CharField(choices=CHOICES1, default="Primavera", max_length=15)
    section=models.IntegerField(choices=CHOICES2)
    year=models.IntegerField()

    def __str__(self):
        return self.title
