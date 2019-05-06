# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
    CHOICES1 = (("Primavera", "Primavera"),("Otoño", "Otoño"),)
    CHOICES2 = ((1,1),(2, 2),)
    CHOICES3 = ((2018,2018),(2019, 2019),(2020,2020),(2021,2021),)
    title=models.CharField(max_length=200)
    code=models.CharField(max_length=20)
    semester=models.CharField(choices=CHOICES1, default="Primavera", max_length=15)
    section=models.IntegerField(choices=CHOICES2,default=1)
    year=models.CharField(max_length=4,default="2019")

    def __str__(self):
        return self.title

class Student(models.Model):
    """Modelo que representa a los estudiantes"""
    first_name= models.CharField(max_length=100, help_text='Ingrese el(los) nombre(s) del estudiante (Ej: Juan Pedro)')
    family_name= models.CharField(max_length=100, help_text='Ingrese el(los) apellido(s) del estudiante (Ej: Pérez González)')

    # Un estudiante puede pertencer a más de un equipo a la vez, y un equipo puede tener más de un estudiante a la vez
    # Esto está dado por la cantidad de cursos y de evaluaciones en las que puede estar
    team= models.ManyToManyField('Team', help_text='Seleccione un equipo para el estudiante');

    class Meta:
        unique_together= ('first_name', 'family_name');
        ordering= ['family_name', 'first_name'];

    def __str__(self):
        return f'{self.family_name}, {self.first_name}';

class Team(models.Model):
    """Modelo que representa a los equipos"""
    name= models.CharField(max_length=200, help_text='Ingrese el nombre del equipo (Ej: ReAL Soluciones)');

    # Un equipo pertenece a lo más a un curso, pero un curso puede tener más de un equipo
    course= models.ForeignKey('Course', on_delete=models.CASCADE)

    class Meta:
        ordering= ['course', 'name']

    def __str__(self):
        return self.name;



