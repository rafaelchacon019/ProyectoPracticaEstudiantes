from django.db import models
from django.db.models.deletion import CASCADE
from api.maestro.models import maestro

# Create your models here.
class materias(models.Model):
    nombre = models.CharField(max_length=50)
    maestro = models.ForeignKey(maestro, models.CASCADE)