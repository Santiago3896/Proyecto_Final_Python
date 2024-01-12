from django.db import models
from ckeditor.fields import RichTextField

class Language(models.Model):
    nombre = models.CharField(max_length=10)
    creador = models.CharField(max_length=15)
    version = models.IntegerField()
    descripcion = models.TextField()
    
    
    def __str__(self):
        return f"{self.nombre}"

class Framework(models.Model):
    nombre = models.CharField(max_length=10)
    languages = models.CharField(max_length=15)
    descripcion = RichTextField()
    fecha_creacion = models.DateField()
    imgFramework = models.ImageField(upload_to='framework', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre}"