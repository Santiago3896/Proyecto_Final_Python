from django import forms

class CreacionLanguages(forms.Form):
    nombre = forms.CharField(max_length=10)
    creador = forms.CharField(max_length=15)
    version = forms.IntegerField()
    descripcion = forms.CharField(max_length=10)
    
    
class CreacionFramework(forms.Form):
    nombre = forms.CharField(max_length=10)
    languages = forms.CharField(max_length=15)
    descripcion = forms.CharField(max_length=10)






    