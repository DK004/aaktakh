from django.contrib import admin
from django.urls import path
from aaktakh import views

urlpatterns = [
    path("", views.index, name ='home'),
    path("index.html", views.index, name='home'),
    path("about.html", views.about, name='about'),
]
