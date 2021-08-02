from rest_framework import serializers
from .models import maestro
from api.materias.models import materias

class MaestroSerializer(serializers.ModelSerializer):
    class Meta:
        model = maestro
        fields = ('nombre','apellido')

class MaestroGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = maestro
        fields = '__all__'

class AllMateriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = materias
        fields = ('id','nombre')

class MixMaestrosMateriasSerializer(serializers.ModelSerializer):
    materia = AllMateriasSerializer(many=True, read_only=True, source='materias_set')
    class Meta:
        model = maestro
        fields = ('id', 'nombre','materia')