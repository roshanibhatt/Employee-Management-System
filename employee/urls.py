
from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path("login/",views.login_view,name='login'),
    path("register/",views.register_view,name='register'),
    path("logout/",views.logout_view,name='logout'),
    path('',views.home,name='home'),


    
]
