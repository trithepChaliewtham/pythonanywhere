from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from . import *






urlpatterns = [

    # name = ตัวแปรใน html <a href "{% url 'name' %}"">

    path('', views.index, name='home'),
   
    path('index',views.index),
   
    path('register', views.signup, name='register'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    

    path('LogIn',auth_views.LoginView.as_view(template_name='myweb/LogIn.html'),name='LogIn'),


    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]