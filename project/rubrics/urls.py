from django.conf.urls import url
from .import views

app_name='rubrics'
urlpatterns=[
    url(r'^$', views.rubric_admin, name="rubrics")
]
