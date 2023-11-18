from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from navegadoresWebs.models import Navegador

class navegadores(ListView):
    model = Navegador
    context_object_name = "listado_navegadores"
    template_name = "navegadores/navegadores.html"
    
class CreacionNavegadores(CreateView):
    model = Navegador
    template_name = "navegadores/creacionNavegadores.html"
    fields = ["nombre", "version", "fecha_creacion"]
    success_url = reverse_lazy("navegadores")
    
