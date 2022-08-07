from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('' ,  home  , name="home"),
    path('login' ,  login , name="login"),
    path('register' ,  register  , name="register"),
    path('token' ,  token  , name="token"),
    path('success' ,  success  , name="success"),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error' ,  error_page  , name="error"),
]