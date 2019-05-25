from django.conf.urls import url
from .import views

app_name='evaluation'

urlpatterns=[
    url(r'^$', views.evaluation_list, name="evaluation"),
    url(r'^delete/$', views.delete_evaluation, name='delete_evaluation'),
]