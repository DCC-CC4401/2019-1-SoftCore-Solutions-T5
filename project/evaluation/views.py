from django.shortcuts import render

# Create your views here.

def evaluation_list(request):
    return render(request,'evaluation/evaluation_list.html',{'evaluation':evaluation})