from django.db import models

from courses.models import Course, Student, Team

from rubrics.models import Rubric

from accounts.models import Account


# Create your models here.
class Evaluation(models.Model):
    name= models.CharField(max_length=200)
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

    def __str__(self):
        return self.evaluation_name.name + '-' + self.account.nombre + ' ' + self.account.appellido


class Evaluation_Student(models.Model):
    evaluation_id = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade = models.IntegerField()

    def __str__(self):
        return self.evaluation_id.name + '-' + self.student.nombre + ' ' + self.student.appellido