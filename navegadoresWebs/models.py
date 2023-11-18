from django.db import models

class Navegador(models.Model):
    nombre = models.CharField(max_length=10)
    version = models.IntegerField()
    fecha_creacion = models.DateField()
    

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.version} - {self.fecha_creacion}"
