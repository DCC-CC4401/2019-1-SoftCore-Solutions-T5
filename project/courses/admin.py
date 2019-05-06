# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Course, Student, Team

from django.contrib import admin

# Register your models here.

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Team)
