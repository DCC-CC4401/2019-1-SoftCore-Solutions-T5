from django.shortcuts import render

# Create your views here.
from .models import Evaluation

def evaluation_list(request):
    evaluation= Evaluation.objects.all().order_by('init_date')
    return render(request,'evaluation/evaluation_list.html',{'evaluation':evaluation})
