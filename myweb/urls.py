from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from . import *






urlpatterns = [

    # name = ตัวแปรใน html <a href "{% url 'name' %}"">

    path('', views.LogIn, name="LogIn-First"),
    path('index', views.index, name='home'),
    path('ViewPrice', views.ViewPrice, name='ViewPrice'),
    path('CheckInform', views.CheckInform, name='CheckInform'),
   
    path('register', views.signup, name='register'),

    #--------------------------- log in ---------------------------#
    path('logout', auth_views.LogoutView.as_view(template_name='myweb/LogIn.html'), name='logout'),
    
    #--------------------------- log out ---------------------------#
    path('LogIn',auth_views.LoginView.as_view(template_name='myweb/LogIn.html'),name='LogIn'),
    
    
   

]