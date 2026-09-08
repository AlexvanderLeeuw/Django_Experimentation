from django.urls import path
from experimentation import views

urlpatterns = [
    path("", views.hi, name="home"),
]