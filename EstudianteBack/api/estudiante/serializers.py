from rest_framework import serializers
from .models import estudiante


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = estudiante
        fields = ('nombre','apellido','maestro','materias','notas')

class EstudianteGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = estudiante
        fields = '__all__'



        