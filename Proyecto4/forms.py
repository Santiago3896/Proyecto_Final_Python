from django import forms

class CreacionLanguagesFormulario(forms.Form):
    nombre = forms.CharField(max_length=10)
    creador = forms.CharField(max_length=15)
    version = forms.IntegerField()
    descripcion = forms.CharField(max_length=10)
    
    
class CreacionFrameworkFormulario(forms.Form):
    nombre = forms.CharField(max_length=10)
    languages = forms.CharField(max_length=15)
    descripcion = forms.CharField(max_length=10)

class BusquedaLanguagesFormulario(forms.Form):
    nombre = forms.CharField(max_length=10, required=False)





    