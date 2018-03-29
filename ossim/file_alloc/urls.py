from django.conf.urls import url,include
from django.contrib import admin
from . import views

app_name = 'file_alloc'
urlpatterns =[

    url(r'^$',views.home.as_view() ),

]
