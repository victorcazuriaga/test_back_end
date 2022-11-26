from django.urls import path
from . import views

urlpatterns = [
    path("reader", views.ReaderView.as_view())
]
