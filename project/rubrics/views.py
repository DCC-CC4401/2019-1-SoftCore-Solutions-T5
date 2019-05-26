# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import *

from .forms import *

from django.shortcuts import render, redirect

# Create your views here.


def rubrics_list(request):
    if request.POST:
        data = request.POST
        name = data['name']
        mi = data['dur_min']
        ma = data['dur_max']
        t = data['table']
        t = t.replace('\t', '')
        rows = t.split('\n')
        rub = []
        for row in rows[:len(rows)-1]:
            r = row.split(',')
            print(r)
            rub.append(r)

        rubric = Rubric.objects.all()
        create = True
        for r in rubric:
            if r.name == name:
                create = False
        if create:
            ru = Rubric.objects.create(name=name, duration_min=mi, duration_max=ma, state=False)
            ru.set_rubric(rub)
            ru.save()

    rubrics = Rubric.objects.all()
    return render(request,'rubrics/rubrics_list.html', {'rubrics': rubrics})


def create_rubric(request):
    return render(request, 'rubrics/rubrics_create.html')


def rubric_details(request, rubric_key):
    rubric = Rubric.objects.get(name=rubric_key)
    rub = rubric.get_rubric()
    return render(request, 'rubrics/rubrics_details.html', {'rubric': rubric, 'levels': rub[0], 'rows': rub[1:]})


def rubric_modify(request, rubric_key):
    rubric = Rubric.objects.get(name=rubric_key)
    rub = rubric.get_rubric()
    return render(request, 'rubrics/rubrics_modify.html', {'rubric': rubric, 'levels': rub[0], 'rows': rub[1:]})


def rubric_modify_database(request, rubric_key):
    rubric = Rubric.objects.get(name=rubric_key)
    if request.method == 'POST':
        data = request.POST
        name = data['name']
        mi = data['dur_min']
        ma = data['dur_max']
        t = data['table']
        t = t.replace('\t', '')
        rows = t.split('\n')
        table = []
        for row in rows[:len(rows) - 1]:
            r = row.split(',')
            table.append(r)

        rubric.name = name
        rubric.duration_min = mi
        rubric.duration_max = ma
        rubric.set_rubric(table)
        rubric.save()
    rubrics = Rubric.objects.all()
    return render(request, 'rubrics/rubrics_list.html', {'rubrics': rubrics})