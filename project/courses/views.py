# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Course

def courses_list(request):
    courses= Course.objects.all().order_by('semester')
    return render(request, 'courses/courses_list.html',{'courses':courses})

def delete_course(request):
    if request.method=='POST':
        id=request.POST['id_course']
        course=Course.objects.get(id=id)
        course.delete()
    courses= Course.objects.all().order_by('semester')
    return render(request, 'courses/courses_list.html',{'courses':courses})
