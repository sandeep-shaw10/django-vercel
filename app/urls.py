from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.index, name="about"),
    path("blog/", views.index, name="blog"),
]