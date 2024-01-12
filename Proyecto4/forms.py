from django import forms
from ckeditor.fields import RichTextFormField

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
    descripcion = RichTextFormField()
    fecha_creacion = forms.DateField()
    imgFramework = forms.ImageField(required=False)
    
class CreacionFrameworkFormulario(Frameworks):
    ...

class ActualizarFrameworkFormulario(Frameworks):
    ...

class BusquedaLanguagesFormulario(forms.Form):
    nombre = forms.CharField(max_length=10, required=False)
    
class BusquedaFrameworksFormulario(forms.Form):
    nombre = forms.CharField(max_length=10, required=False)






    