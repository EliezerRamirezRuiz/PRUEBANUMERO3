from django.urls import path
from rest_auth.views import login

urlpatterns = [
    path('login',login, name="login"),
]