from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


from myweb import views

urlpatterns = [
    
    #path('', views.index),
    path('admin/', admin.site.urls),
    path('', include('myweb.urls')),
    #path('polls/', include('polls.urls')),

]
