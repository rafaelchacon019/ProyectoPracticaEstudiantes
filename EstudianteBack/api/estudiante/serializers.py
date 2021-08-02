from rest_framework import serializers
from .models import estudiante
from api.maestro.models import maestro
from api.materias.models import materias
from api.notas.models import notas

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = estudiante
        fields = ('nombre','apellido','maestro','materias','notas')

class EstudianteGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = estudiante
        fields = '__all__'

class AllMaestroSerializer(serializers.ModelSerializer):
    class Meta:
        model = maestro
        fields = ('id','nombre')

class AllMateriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = materias
        fields = ('id','nombre')

class AllNotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = notas
        fields = ('id','numeroNota')

class MixTablasSerializer(serializers.ModelSerializer):
    maestro = AllMaestroSerializer(many=True, read_only=True)
    materias = AllMateriasSerializer(many=True, read_only=True)
    notas =  AllNotasSerializer(many=True, read_only=True)

    class Meta:
        model = estudiante
        fields = ('id', 'nombre', 'apellido', 'maestro', 'materias', 'notas')