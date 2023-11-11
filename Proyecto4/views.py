from django.shortcuts import render

# Create your views here.

def Inicio(request):
    
    return render(request,"inicio/Inicio.html")

def About(request):
    
    return render(request,"inicio/About.html")

def Contact(request):
    
    return render(request,"inicio/Contact.html")

def Contact(request):
    
    return render(request,"inicio/Contact.html")

def Languages(request):
    
    return render(request,"inicio/Languages.html")

def Frameworks(request):
    
    return render(request,"inicio/Frameworks.html")