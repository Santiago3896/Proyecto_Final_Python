from django.urls import path

from navegadoresWebs.views import navegadores, CreacionNavegadores

urlpatterns = [
    
    path("navegadores", navegadores.as_view(), name = "navegadores"),
    path("navegadores/crear", CreacionNavegadores.as_view(), name = "crear_navegador"),
    
]