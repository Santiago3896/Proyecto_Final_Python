from django.shortcuts import render, redirect

from Proyecto4.forms import CreacionLanguages, CreacionFramework
from Proyecto4.models import Language, Framework

# Create your views here.

def Inicio(request):
    
    return render(request,"inicio/Inicio.html")

def Languages(request):
    
    if request.method == "POST":
        formularioLanguages = CreacionLanguages(request.POST)
        if formularioLanguages.is_valid():
            info_limpiaLanguages = formularioLanguages.cleaned_data
            
            print(info_limpiaLanguages)
            
            nombre = info_limpiaLanguages.get("nombre")
            creador = info_limpiaLanguages.get("creador")
            version = info_limpiaLanguages.get("version")
            descripcion = info_limpiaLanguages.get("descripcion")
            print(nombre)
            
            languages = Language(nombre = nombre , creador = creador , version = version , descripcion = descripcion)
             
            languages.save()
            return redirect(Inicio)
        else: 
            return render(request, "", {"formularioLanguages": formularioLanguages})
    formulario = CreacionLanguages()
    return render(request,"inicio/Languages.html", {"formulario": formulario})       
    

def Frameworks(request):
    if request.method == "POST":
        formularioFramework = CreacionFramework(request.POST)
        if formularioFramework.is_valid():
            info_limpiaFramework = formularioFramework.cleaned_data
            
            nombre = info_limpiaFramework.get("nombre")
            languages = info_limpiaFramework.get("languages")
            descripcion = info_limpiaFramework.get("descripcion")
            
            framework = Framework(nombre = nombre , languages = languages , descripcion = descripcion)
            framework.save()
            return redirect(Inicio)
        else:
            return render(request, "", {"formularioFramework": formularioFramework}) 
    formularioF = CreacionFramework()
    return render(request,"inicio/Frameworks.html", {"formularioF": formularioF})
            
            
    
    
    return render(request,"inicio/Frameworks.html")


def About(request):
    
    return render(request,"inicio/About.html")

def Contact(request):
    
    return render(request,"inicio/Contact.html")

