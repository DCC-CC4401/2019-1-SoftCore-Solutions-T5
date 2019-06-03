from django.conf.urls import url
from .import views

app_name='evaluation'

urlpatterns=[
    url(r'^$', views.evaluation_list, name="evaluation"),
    url(r'^delete/$', views.delete_evaluation, name='delete_evaluation'),
    url(r'^modify/(?P<evaluation_id>[\w ]+)/$', views.evaluation_modify),
    url(r'^(?P<evaluation_id>[\w ]+)/$', views.evaluation_details),
    url(r'^(?P<evaluation_id>[\w ]+)/evaluate/$', views.evaluate),
    url(r'^(?P<evaluation_id>[\w ]+)/addEvaluator/$', views.add_evaluator),
    url(r'^(?P<evaluation_id>[\w ]+)/deleteEvaluator/$', views.delete_evaluator),
]