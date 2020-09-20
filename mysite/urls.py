from django.contrib import admin
from django.urls import path, include


from myweb import views

urlpatterns = [
    #path('', views.index),
    path('', include('myweb.urls')),
    #path('polls/', include('polls.urls')),
    path('myweb/', include('myweb.urls')),
    path('index', views.index),
    path('LogIn', views.LogIn),
    path('register', views.register),
    path('united', views.united),
    path('admin/', admin.site.urls),
]
