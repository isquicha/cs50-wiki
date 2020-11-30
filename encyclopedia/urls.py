from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.wiki, name="wiki"),
    path("search/", views.search, name="search"),
    path("new", views.new, name="new"),
    path("random", views.random_entry, name="random_entry"),
    path("edit/<str:entry>", views.edit, name="edit"),
]

handler404 = "encyclopedia.views.handler404"
