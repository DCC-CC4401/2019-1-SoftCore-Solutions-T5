from django.conf.urls import url
from .import views

app_name='rubrics'

urlpatterns=[
    url(r'^$', views.rubrics_list, name="rubrics"),
    url(r'^create/$', views.create_rubric, name='create_rubric'),
    url(r'^delete/$', views.delete_rubric, name='delete_rubric'),
    url(r'^details/(?P<rubric_key>[\w-]+)/$', views.rubric_details),
    url(r'^modify/(?P<rubric_key>[\w-]+)/$', views.rubric_modify),
    url(r'^modify_database/(?P<rubric_key>[\w-]+)/$', views.rubric_modify_database),
]
