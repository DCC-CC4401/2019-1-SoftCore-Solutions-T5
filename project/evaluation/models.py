from django.db import models

from courses.models import *

from rubrics.models import *

from accounts.models import *

# Create your models here.
class Evaluation(models.Model):
    name= models.CharField(max_length=200, primary_key=True)
    init_date= models.DateField()
    fin_date= models.DateField()
    rubric= models.ForeignKey(Rubric, on_delete=models.SET_NULL, null=True)
    state= models.BooleanField()

    def __str__(self):
        return self.name

class Evaluation_Course(models.Model):
    evaluation_name=models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)

class Evaluation_Account(models.Model):
    evaluation_name=models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    account=models.ForeignKey(Account, on_delete=models.CASCADE)
    team=models.ForeignKey(Team, on_delete=models.CASCADE)
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
