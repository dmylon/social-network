
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("posts/<str:info>", views.loadPosts, name="load"),
    path("posts", views.newPost, name="newpost"),
    path("pages/<str:username>", views.viewProfile, name="viewProfile"),
    path("following", views.viewFollowing, name="viewFollowing"),
    path("post/<int:id>", views.loadPostById, name="loadPostById"),
    path("follow", views.followUser, name="followUser")
]
