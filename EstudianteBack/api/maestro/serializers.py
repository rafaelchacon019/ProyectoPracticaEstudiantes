from rest_framework import serializers
from .models import maestro
from api.estudiante.models import estudiante


class MaestroSerializer(serializers.ModelSerializer):
    class Meta:
        model = maestro
        fields = ('nombre','apellido')

class MaestroGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = maestro
        fields = '__all__'

class MixEstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = estudiante
        fields = ('id','nombre','apellido')

        