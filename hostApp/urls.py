"""HostMangement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from hostApp import views

urlpatterns = [
    url(r'^userinfo', views.userinfo),
    url(r'^usertype', views.usertype),
    url(r'^hostinfo', views.hostinfo),
    url(r'^testitem', views.test_item),
    url(r'^business', views.usertype),
    url(r'^many_to_many$', views.many_to_many),
    url(r'^many_to_many_edit', views.many_to_many_edit),
    url(r'^test_ajax$', views.test_ajax),
    url(r'^test_ajax1', views.test_ajax1),
    url(r'^edit_data-(\d+)', views.edit_data),
    url(r'^index', views.index),
    url(r'^login', views.login),
]
