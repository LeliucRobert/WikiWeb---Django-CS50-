from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>" , views.entry , name="entry"),
    path("search/" , views.search , name="search"),
    path("new/" , views.newPage , name="new"),
    path("edit/" , views.edit , name="edit"),
    path("saveEdit/" , views.saveEdit , name="saveEdit"),
    path("random/" , views.randomPage , name="random")
]
