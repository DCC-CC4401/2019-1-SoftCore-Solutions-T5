
from django.conf.urls import url, include
from django.contrib import admin
from .import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^courses/',include('courses.urls')),
    url('^accounts/',include('accounts.urls'), name='accounts'),
    url(r'^$', views.homepage),
]
