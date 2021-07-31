from django.db.models import fields
from rest_framework import serializers

from .models import notas

class NotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = notas
        fields = ('numeroNota',)
    
class NotasGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = notas
        fields = '__all__'