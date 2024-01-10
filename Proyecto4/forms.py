from django import forms

class Languages(forms.Form):
    nombre = forms.CharField(max_length=10)
    creador = forms.CharField(max_length=15)
    version = forms.IntegerField()
    descripcion = forms.CharField(max_length=10)
    
    
class CreacionLanguagesFormulario(Languages):
    ...
    
class ActualizarLanguagesFormulario(Languages):
    ...
    
    
class Frameworks(forms.Form):
    nombre = forms.CharField(max_length=10)
    languages = forms.CharField(max_length=15)
    descripcion = forms.CharField(max_length=10)
    # fecha_creacion = forms.DateField()
    # imgFramework = forms.ImageField(required=False)
    
class CreacionFrameworkFormulario(Frameworks):
    ...

class ActualizarFrameworkFormulario(Frameworks):
    ...

class BusquedaLanguagesFormulario(forms.Form):
    nombre = forms.CharField(max_length=10, required=False)
    
class BusquedaFrameworksFormulario(forms.Form):
    nombre = forms.CharField(max_length=10, required=False)






    