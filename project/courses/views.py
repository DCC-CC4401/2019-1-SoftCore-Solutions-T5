# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from .models import Course, Student, Team

from django.shortcuts import render,redirect

from .forms import CourseForm

def courses_list(request):
    if request.method=='POST':
        title = request.POST['title']
        code= request.POST['code']
        semester = request.POST['semester']
        section = request.POST['section']
        year = request.POST['year']
        course = Course.objects.create(title = title, code = code,
                                       semester = semester,
                                       section = section, year = year)
        course.save()
        courses = Course.objects.all().order_by('semester')
        return redirect('/courses', {'courses': courses})
    courses = Course.objects.all().order_by('semester')
    return render(request,'courses/courses_list.html', {'courses': courses})

def delete_course(request):
    if request.method=='POST':
        id=request.POST['id_course']
        course=Course.objects.get(id=id)
        course.delete()
    courses= Course.objects.all().order_by('semester')
    return render(request, 'courses/courses_list.html',{'courses':courses})


def course_details(request, course_key):
    """Para cuando se seleccione el botón de curso"""
    course_keys= course_key.split("-")
    course= Course.objects.get(code=course_keys[0], section=course_keys[1], year=course_keys[2], semester=course_keys[3])
    teamsList= Team.objects.filter(course=course)
    students=Student.objects.all()
     # filter puede retornar más de un parámetro
    lenTeams= teamsList.count()
    print(lenTeams)
    return render(request, 'courses/course_details.html', {'course': course, 'teams': teamsList, 'lenTeams': lenTeams, 'students': students})

def saveCourse(request):
    """Para cuando se envíe la información del nuevo curso por post"""
    # Forma de invocar varoables post: variable= request.POST['nombre_del_campo']
