# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def rubric_admin(request):
    return render(request, 'rubrics/rubrics_admin.html')