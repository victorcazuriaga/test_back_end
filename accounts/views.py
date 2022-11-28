from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from .models import User
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login
import ipdb
# Create your views here.


class CreateUser(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


def register_user(request):
    if request.method == "GET":
        forms = RegisterForm(request.POST)
        context = {"forms": RegisterForm}
        return render(request, "register.html", context=context)
    else:
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
    user = User.objects.filter(email=email).first()
    if user:
        return HttpResponse("e-mail já cadastrado")
    user = User.objects.create_user(
        username=username, email=email, password=password)
    user.save()

    return HttpResponse("usuário cadastrado com sucesso")


def login_user(request):
    if request.method == "GET":
        forms = LoginForm(request.POST)
        context = {"forms": LoginForm}
        return render(request, "login.html", context=context)
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponse("logado")
        else:
            return HttpResponse("Login ou senha inválido")


def authetificated(request):
    if request.user.is_authenticated:
        return HttpResponse("test")
    return HttpResponse("precisa logar")
