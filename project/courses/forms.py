# -*- coding: utf-8 -*-

from django import forms

class CourseForm(forms.Form):
    title = forms.CharField(max_length=100,required = True)
    code=forms.CharField(max_length=100,required = True)
    semester = forms.ChoiceField(widget = forms.Select(),
                 choices = ([('Primavera','Primavera'), ('Otoño','Otoño')]))
    section=forms.ChoiceField(widget = forms.Select(),
                 choices = ([('1','1'), ('2','2')]), initial='1')
    year=forms.CharField(max_length=4,initial="2019")
