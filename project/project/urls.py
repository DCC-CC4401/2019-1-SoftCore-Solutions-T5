
from django.conf.urls import url, include
from django.contrib import admin
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^courses/',include('courses.urls')),
    url('^accounts/',include('accounts.urls'), name='accounts'),
    url(r'^home$', views.homepage),
    url(r'^$',include('accounts.urls')),
]

urlpatterns+= staticfiles_urlpatterns()
