from importlib.util import module_for_loader
from django.db import models

# Create your models here.


class Empleado(models.Model):
    codigo=models.CharField(primary_key=True, max_length=20)
    nombre=models.CharField(max_length=50)
    telefono=models.PositiveBigIntegerField()
    correo=models.CharField(max_length=50)
    
    def __str__(self):
        texto= "{0} ({1})"
        return texto.format(self.nombre, self.codigo)