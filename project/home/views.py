from django.http import HttpResponse
from django.shortcuts import render

from evaluation.models import Evaluation, Evaluation_Course, Evaluation_Account
from courses.models import Course, Team
from rubrics.models import Rubric
from accounts.models import Account

def homepage(request):
    eval = []
    evaluations = Evaluation.objects.order_by('-init_date')

    courses = Course.objects.all()
    rubrics = Rubric.objects.all()

    user_email=request.user.email
    acc_user = Account.objects.get(correo=user_email)

    ### Seleccionar las evaluaciones, junto con la info del curso correspondiente

    c = 0

    for evaluation in evaluations:
        eval_course = Evaluation_Course.objects.get(evaluation_name=evaluation)
        team_count = len(Team.objects.filter(course=eval_course.course))
        accounts =[]
        eval_account = Evaluation_Account.objects.filter(evaluation_name=evaluation)
        for e in eval_account:
            accounts.append(e.account)
        if acc_user in accounts and c<10:
            eval.append((evaluation, eval_course, team_count, eval_account))
            c+=1

    return render(request,'home/homepage.html', {'evaluations': eval,
                                                 'courses': courses,
                                                 'rubrics': rubrics})
