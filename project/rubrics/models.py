# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Rubric(models.Model):
    name=models.CharField(max_length=200, primary_key=True)
    duration_min=models.PositiveSmallIntegerField()
    duration_max = models.PositiveSmallIntegerField()
    state = models.BooleanField()

    def __str__(self):
        return self.name


class Criteria(models.Model):
    key = models.CharField(default='0', max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    rubric = models.ForeignKey(Rubric, on_delete=models.CASCADE)

    def __str__(self):
        return "name: {}, rubric: {}".format(self.name, self.rubric)


class Field(models.Model):
    description = models.CharField(max_length=200)
    level = models.FloatField()
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)

    def __str__(self):
        return "desc: {}, level: {}".format(self.description, self.level)
