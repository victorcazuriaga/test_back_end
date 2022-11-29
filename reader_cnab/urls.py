from django.urls import path
from . import views

urlpatterns = [
    path("reader", views.ReaderView.as_view()),
    path("upload", views.update_file, name="page_upload"),
    path("data", views.get_all_register, name="page_data"),
]
