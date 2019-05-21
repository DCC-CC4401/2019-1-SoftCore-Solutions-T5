# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import *

from django.shortcuts import render

# Create your views here.


def rubrics_list(request):
    rubrics = Rubric.objects.all()
    return render(request,'rubrics/rubrics_list.html', {'rubrics': rubrics})


def create_rubric(request):
    return render(request, 'rubrics/rubrics_create.html')

