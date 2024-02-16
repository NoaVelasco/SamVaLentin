from django.urls import path
from formulario import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("results/", views.results, name="results"),
    path("reset", views.reset, name="reset")
]
