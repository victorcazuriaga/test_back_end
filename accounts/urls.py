from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from . import views

urlpatterns = [
    path('register', views.CreateUser.as_view()),
    path('login', ObtainAuthToken.as_view()),
    path('register_page', views.register_user, name="page_register"),
    path('login_page', views.login_user, name="page_login"),
    path('auth', views.authetificated, name="auth"),



]
