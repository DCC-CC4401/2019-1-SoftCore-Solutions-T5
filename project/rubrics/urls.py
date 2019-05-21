from django.conf.urls import url
from .import views

app_name='rubrics'

urlpatterns=[
    url(r'^$', views.rubrics_list, name="rubrics"),
    url(r'^create/$', views.create_rubric, name='create_rubric'),
]
