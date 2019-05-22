# -*- coding: utf-8 -*-

from django import forms


class RubricForm(forms.Form):
    name = forms.CharField(max_length=200)
    duration_min = forms.IntegerField()
    duration_max = forms.IntegerField()

