# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import Course
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
