from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path( 'login_views/' ,  views.login_views , name='login_views'),
    path('sign_views/' , views.sign_views , name = 'signviews')  
]
