from django.conf.urls import url
from django.contrib import admin
from django.urls import path , include
from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]
