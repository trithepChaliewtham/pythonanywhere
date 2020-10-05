from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views




urlpatterns = [
    
    #path('', views.index),
    path('admin/', admin.site.urls),
    path('', include('myweb.urls')),
    #path('polls/', include('polls.urls')),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
