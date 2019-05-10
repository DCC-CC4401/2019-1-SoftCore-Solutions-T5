from django.conf.urls import url
from django.contrib import admin
from .import views

app_name='accounts'

urlpatterns=[
url(r'^signup/$', views.signup_view, name="signup"),
url(r'^$',views.login_view,name="login"),
url(r'^signup/(?P<account_key>[\w-]+)/$', views.account_details),
url(r'^logout$',views.logout_view,name="logout"),

]
