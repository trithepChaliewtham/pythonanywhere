from django.urls import path

from . import views

urlpatterns = [

    # name = ตัวแปรใน html <a href "{% url 'name' %}"">

    path('', views.index, name='index'),
    path('index', views.index, name='index'),

    path('LogIn', views.LogIn, name='LogIn'),
    path('register', views.register, name='register'),

    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]