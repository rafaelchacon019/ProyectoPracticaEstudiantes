from django.db import models

# Create your models here.
class notas(models.Model):
    numeroNota = models.BigIntegerField(blank=True, null=True)