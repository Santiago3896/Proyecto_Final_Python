from django.shortcuts import render, redirect

from Proyecto4.forms import CreacionLanguages, CreacionFramework
from Proyecto4.models import Language, Framework

# Create your views here.

def Inicio(request):
    listado_languages = Language.objects.all()
    return render(request,"inicio/Inicio.html",{"listadoL": listado_languages})

def Languages(request):
    listadoL = Language.objects.all()
    print(listadoL)
    return render(request,"inicio/Languages.html",{"listadoL": listadoL})

def Frameworks(request):
    listado_frameworks = Framework.objects.all()
    print("pasando")
    return render(request,"inicio/Frameworks.html",{"listadoF": listado_frameworks})

def Creacion_Languages(request):
    
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
            print(languages)
            return redirect(Inicio)
        else: 
            print("pasando por aca")
            return render(request,"", {"formularioLanguages": formularioLanguages})
    formularioL = CreacionLanguages()
    return render(request,"inicio/CreacionLanguages.html", {"formularioLl": formularioL})       
    

def Creacion_Frameworks(request):
    
    if request.method == "POST":
        formularioFramework = CreacionFramework(request.POST)
        if formularioFramework.is_valid():
            info_limpiaFramework = formularioFramework.cleaned_data
            # AGARRO EL DATO DEL FORM Y LO GUARDO EN VARIABLE
            nombre = info_limpiaFramework.get("nombre")
            languages = info_limpiaFramework.get("languages")
            descripcion = info_limpiaFramework.get("descripcion")
            # DONDE DIGA TAL COSA EN EL MODELO REMPLAZALO POR TAL VARIABLE. SAVE GUARDA EN EL MODELO
            framework = Framework(nombre = nombre , languages = languages , descripcion = descripcion)
            framework.save()
            # REDIRIGIR A LA VIEW INICIO
            return redirect(Inicio)
        else:
            # SI NO ES VALIDO EL FORMULARIO, SE MUESTRA EL ERROR PERO NO ME ESTA FUNCIONANDO- ARREGLAR -
            return render(request, "", {"formularioFramework": formularioFramework}) 
    formularioF = CreacionFramework()
    # LE PASO EL FORMULARIO VACIO ABAJO, PORQUE LA PRIMER VISTA VIENE POR GET
    return render(request,"inicio/CreacionFrameworks.html", {"formularioFf": formularioF})


def About(request):
    
    return render(request,"inicio/About.html")

def Contact(request):
    
    return render(request,"inicio/Contact.html")

