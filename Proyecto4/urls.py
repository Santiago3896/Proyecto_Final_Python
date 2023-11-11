from django.contrib import admin
from django.urls import path
from Proyecto4.views import Inicio, About, Contact,Frameworks,Languages

urlpatterns = [
    path("",Inicio,name = "inicio"),
    path("/About",About,name = "about"),
    path("/Contact",Contact,name = "contact"),
    path("/Languages",Languages,name = "languages"),
    path("/Frameworks",Frameworks,name = "frameworks"),
]