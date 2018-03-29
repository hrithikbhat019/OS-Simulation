
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^',include('home.urls')),
    url(r'^sockets/',include('sockets.urls')),
    url(r'^synchro/',include('synchro.urls'))
]
