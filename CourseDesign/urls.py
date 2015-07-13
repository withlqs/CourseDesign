"""CourseDesign URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from StuInfo.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^add/$', add),
    url(r'^search/$', search),
    url(r'^view/$', view),
    url(r'^delete/$', delete),
    url(r'^modify/$', modify),
    url(r'^successful/$', successful),
    url(r'^accounts/login/$', views.login),
    url(r'^accounts/logout/$', logout_view),
    url(r'^accounts/register/$', register),
    url(r'^accounts/profile/$', logined),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
]
