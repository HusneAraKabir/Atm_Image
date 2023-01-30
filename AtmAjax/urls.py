from django.contrib import admin
from django.urls import path
from .views import GetCardInfo, RegisterUser, LoginUser

urlpatterns = [
    path('get-card-info/', GetCardInfo, name="GetCardInfo"),
    path('register-user/', RegisterUser, name="RegisterUser"),
    path('login-user/', LoginUser, name="LoginUser"),
]
