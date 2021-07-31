from django.db import models
from api.maestro.models import maestro
from api.materias.models import materias
from api.notas.models import notas

# Create your models here.
class estudiante(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    maestro = models.ManyToManyField(maestro)
    materias = models.ManyToManyField(materias)
    notas = models.ManyToManyField(notas)