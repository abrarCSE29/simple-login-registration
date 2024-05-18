from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home , name="home"),
    path('login', views.login, name="login"),
    path('signup',views.signup, name="signup"),
    path('processRequest', views.processRequest, name="processRequest"),
    path('getCredentials', views.getCredentials, name="getCredentials"),
    path('dashboard', views.dashboard, name="dashboard"),
]
