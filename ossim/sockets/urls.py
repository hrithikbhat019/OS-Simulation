from django.conf.urls import url,include
from django.contrib import admin
from . import views

app_name = 'synchro'
urlpatterns =[

    url(r'^$',views.main ),
    url(r'^tcp$',views.tcp),
    url(r'^udp$',views.udp),


]
