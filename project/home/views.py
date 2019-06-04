from django.http import HttpResponse
from django.shortcuts import render

from evaluation.models import Evaluation, Evaluation_Course, Evaluation_Account
from courses.models import Course, Team
from rubrics.models import Rubric
from accounts.models import Account

def homepage(request):
    if request.user.is_authenticated and request.user.is_superuser:
        try:
            user = request.user
            email = user.email
            acc = Account.objects.get(correo=email)
        except Account.DoesNotExist:
            username = user.username
            password = user.password
            acc = Account.objects.create(nombre=username, appellido='', correo=email, clave=password, is_superuser=True)
            acc.save()
    evaluations = Evaluation.objects.order_by('-init_date')

    courses = Course.objects.all()
    rubrics = Rubric.objects.all()

    user_email=request.user.email
    acc_user = Account.objects.get(correo=user_email)

    ### Seleccionar las evaluaciones, junto con la info del curso correspondiente

    c = 0

    eval = []

    for evaluation in evaluations:
        try:
            eval_course = Evaluation_Course.objects.get(evaluation_name=evaluation)
            team_count = len(Team.objects.filter(course=eval_course.course))
            eval_account = Evaluation_Account.objects.filter(evaluation_name=evaluation, account=acc_user)
            if len(eval_account)==1 and c<10:
                eval.append((evaluation, eval_course, team_count, eval_account))
                c+=1
        except Evaluation_Course.DoesNotExist:
            continue
    return render(request,'home/homepage.html', {'evaluations': eval,
                                                 'courses': courses,
                                                 'rubrics': rubrics})