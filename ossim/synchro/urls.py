from django.conf.urls import url,include
from django.contrib import admin
from . import views

app_name = 'synchro'
urlpatterns =[
    url(r'^semaphores/$', views.semaphores, name='semaphores'),
    url(r'^semaphores/demo/(?P<pk>[0-9]+)/$', views.sem_demo, name='sem_demo'),
]
