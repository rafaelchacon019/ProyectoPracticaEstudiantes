from django.db.models import fields
from rest_framework import serializers

from .models import materias
from api.maestro.models import maestro

class MateriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = materias
        fields = ('nombre', 'maestro')
    
class MateriasGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = materias
        fields = '__all__'

class allMaestroSerializer(serializers.ModelSerializer):
    class Meta:
        model = maestro
        fields = ('id','nombre','apellido')