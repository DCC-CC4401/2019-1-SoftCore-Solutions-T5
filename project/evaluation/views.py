#-*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.
from .models import Evaluation, Evaluation_Course, Evaluation_Account
from courses.models import Course
from rubrics.models import Rubric

# Para trabajar con queries complejas, como con negación
from django.db.models import Q


def evaluation_list(request):
    if request.method == 'POST':
        titulo = request.POST['title']
        init_date = request.POST['init_date']
        fin_date = request.POST['fin_date']
        rubric_name = request.POST['rubric']
        course_info = request.POST['course'].split('-')

        code = course_info[0]
        section = course_info[1]
        semester = course_info[2]
        year = course_info[3]

        rubric_eval = Rubric.objects.get(name=rubric_name)
        new_eval = Evaluation.objects.create(name=titulo, init_date=init_date, fin_date=fin_date, rubric=rubric_eval, state=True)
        new_eval.save()

        course_eval = Course.objects.get(code=code, section=section, semester=semester, year=year)
        new_eval_course = Evaluation_Course.objects.create(evaluation_name=new_eval, course=course_eval)
        new_eval_course.save()

    eval = []
    evaluations = Evaluation.objects.all().order_by('init_date')

    courses = Course.objects.all()
    rubrics = Rubric.objects.all()

    ### Seleccionar las evaluaciones, junto con la info del curso correspondiente
    for evaluation in evaluations:
        eval_course = Evaluation_Course.objects.get(evaluation_name=evaluation)
        eval.append((evaluation, eval_course))

    return render(request,'evaluation/evaluation_list.html', {'evaluations': eval,
                                                              'courses': courses,
                                                              'rubrics': rubrics})


def delete_evaluation(request):
    if request.method == 'POST':
        eval_name = request.POST['eval_name']
        code_course = request.POST['code_course']
        section_course = request.POST['section_course']
        semester_course = request.POST['semester_course']
        year_course = request.POST['year_course']

        course = Course.objects.get(code=code_course, section=section_course, semester=semester_course, year=year_course)
        del_evaluation = Evaluation.objects.get(name=eval_name)

        eval_course = Evaluation_Course.objects.get(evaluation_name=del_evaluation, course=course)
        eval_course.delete()
        del_evaluation.delete()
    eval = []
    evaluations = Evaluation.objects.all().order_by('init_date')

    courses = Course.objects.all()
    rubrics = Rubric.objects.all()

    # Seleccionar las evaluaciones, junto con la info del curso correspondiente
    for evaluation in evaluations:
        eval_course = Evaluation_Course.objects.get(evaluation_name=evaluation)
        eval.append((evaluation, eval_course))

    return render(request, 'evaluation/evaluation_list.html', {'evaluations': eval,
                                                               'courses': courses,
                                                               'rubrics': rubrics})


def evaluation_details(request, evaluation_name):
    evaluation= Evaluation.objects.get(name=evaluation_name)
    eval_course= Evaluation_Course.objects.get(evaluation_name=evaluation_name)
    course= eval_course.course
    return render(request, 'evaluation/evaluation_details.html', {'evaluation': evaluation,
                                                                  'course': course})


def evaluation_modify(request, evaluation_name):
    evaluation= Evaluation.objects.get(name=evaluation_name)
    eval_course = Evaluation_Course.objects.get(evaluation_name=evaluation_name)
    course = eval_course.course
    rubric= evaluation.rubric
    otherCourses= Course.objects.filter(~Q(course=course))
    otherRubrics=Rubric.objects.filter(~Q(rubric=rubric))
    return render(request, 'evaluation/evaluation_modify.html', {'evaluation': evaluation,
                                                                 'course': course,
                                                                 'otherCourses': otherCourses,
                                                                 'otherRubrics': otherRubrics})