# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Course, Student, Team

def courses_list(request):
    """View para la página de cursos"""
    
    courses= Course.objects.all().order_by('semester')
    
    return render(request, 'courses/courses_list.html', {'courses':courses})

def course_details(request, course_key):
    """Para cuando se seleccione el botón de curso"""
    course_keys= course_key.split("-")
    course= Course.objects.get(code=course_keys[0], section=course_keys[1], year=course_keys[2], semester=course_keys[3])
    teamsList= Team.objects.filter(course=course) # filter puede retornar más de un parámetro
    lenTeams= teamsList.count()
    print(lenTeams)
    return render(request, 'courses/course_details.html', {'course': course, 'teams': teamsList, 'lenTeams': lenTeams})
