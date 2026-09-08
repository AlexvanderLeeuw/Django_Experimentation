from django.urls import path
from experimentation import views

urlpatterns = [
    path("", views.home, name="home"),
]