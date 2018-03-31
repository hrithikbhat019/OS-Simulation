from django.conf.urls import url,include
from django.urls import path
from django.contrib import admin
from . import views

app_name = 'file_alloc'
urlpatterns =[

    path('contiguous',views.contiguous.as_view() ),
    path('linked',views.linked.as_view() ),

]
