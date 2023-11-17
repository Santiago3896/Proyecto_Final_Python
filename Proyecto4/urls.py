from django.contrib import admin
from django.urls import path
from Proyecto4.views import Inicio, About, Contact, Creacion_Frameworks, Creacion_Languages, Languages,Frameworks

urlpatterns = [
    path("",Inicio,name = "inicio"),
    path("/About",About,name = "about"),
    path("/Contact",Contact,name = "contact"),
    path("/Languages",Languages,name = "languages"),
    path("/Frameworks",Frameworks,name = "frameworks"),
    path("/CreacionFrameworks",Creacion_Frameworks,name = "CreacionFrameworks"),
    path("/CreacionLanguages",Creacion_Languages,name = "CreacionLanguages"),
    
    # (EL PATH QUE QUIERO PONERLE (Es indistinto)  -- LA VIEW QUE QUIERO MOSTRAR -- PARA CONECTAR CON EL TEMPLATE BASE (Opcional))
]