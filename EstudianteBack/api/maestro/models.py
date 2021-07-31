from django.db import models

# Create your models here.
class maestro(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)