from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("blog/", views.blog, name="blogs"),
    path("blog/<slug>", views.getBlog, name="get_blog"),
]