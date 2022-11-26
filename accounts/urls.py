from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from . import views

urlsurlpatterns = [
    path('/register', views.CreateUser.as_view()),
    path('/login', ObtainAuthToken.as_view())
]
