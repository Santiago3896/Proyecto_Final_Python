from django.contrib import admin
from django.urls import path
from Proyecto4.views import inicio

urlpatterns = [
    path("",inicio,name = "inicio"),
]