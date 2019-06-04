from __future__ import unicode_literals
from .models import Evaluation, Evaluation_Course, Evaluation_Account, Evaluation_Student, Evaluation_Student_Presented

from django.contrib import admin

# Register your models here.

admin.site.register(Evaluation)
admin.site.register(Evaluation_Course)
admin.site.register(Evaluation_Account)
admin.site.register(Evaluation_Student)
admin.site.register(Evaluation_Student_Presented)