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
        rows = t.split('%\n%')
        rub = [rows[0].split('%,%')]
        for row in rows[1:len(rows)]:
            r = row.split('%,%')
            print(r)
            if r[0] != '':
                rub.append(r)

        empty_column_indexs = []
        for i in range(1, len(rub[0])):
            if rub[0][i] == '':
                empty_column_indexs.append(i)
        for idx in empty_column_indexs[::-1]:
            for row in rub:
                row.pop(idx)

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
    rubric.delete()

    if request.method == 'POST':
        data = request.POST
        name = data['name']
        mi = data['dur_min']
        ma = data['dur_max']
        t = data['table']
        t = t.replace('\t', '')
        rows = t.split('%\n%')
        rub = [rows[0].split('%,%')]
        for row in rows[1:len(rows)]:
            r = row.split('%,%')
            if r[0] != '':
                rub.append(r)
        empty_column_indexs = []
        for i in range(1, len(rub[0])):
            if rub[0][i] == '':
                empty_column_indexs.append(i)
        for idx in empty_column_indexs[::-1]:
            for row in rub:
                row.pop(idx)

        create = True
        rubric = Rubric.objects.all()
        for r in rubric:
            if r.name == name:
                create = False
        if create:
            ru = Rubric.objects.create(name=name, duration_min=mi, duration_max=ma, state=False)
            ru.set_rubric(rub)
            ru.save()
    rubrics = Rubric.objects.all()
    return render(request, 'rubrics/rubrics_list.html', {'rubrics': rubrics})
