from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from . import *






urlpatterns = [

    # name = ตัวแปรใน html <a href "{% url 'name' %}"">

    path('', views.LogIn, name="LogIn-First"),

    path('index', views.index, name='home'),

    path('searchfruit', views.search, name='searchfruit'),

    path('AllFruit', views.showFruit, name='AllFruit'),

    path('showfruit', views.showFruit, name='showfruit'),

    path('addfarm', views.addfarm, name='addfarm'),

    path('addfruit',views.addfruit, name ="addfruit"),

    path('CheckInform', views.CheckInform, name='CheckInform'),
   
    path('register', views.signup, name='register'),

    #--------------------------- log in ---------------------------#
    path('logout', auth_views.LogoutView.as_view(template_name='myweb/LogIn.html'), name='logout'),
    
    #--------------------------- log out ---------------------------#
    path('LogIn',auth_views.LoginView.as_view(template_name='myweb/LogIn.html'),name='LogIn'),
    
    
   

]