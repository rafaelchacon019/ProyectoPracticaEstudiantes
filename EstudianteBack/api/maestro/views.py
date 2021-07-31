from django.shortcuts import get_object_or_404, render
from rest_framework import serializers, status
from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import maestro
from.serializers import MaestroSerializer, MaestroGetSerializer, MixEstudianteSerializer

# Create your views here.
class MaestroViews(APIView):

    def get(self, request):
        try:
            listas = maestro.objects.all()
            serializer = MaestroGetSerializer(listas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_503_SERVICE_UNAVAILABLE)

    def post(self, request):
        try:
            serializer = MaestroSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(['Elemento insertado.'], status=status.HTTP_200_OK)
            else:
                return Response(['Error 400'], status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_503_SERVICE_UNAVAILABLE)

    def put(self, request, id=None):
        try:
            lista_act = get_object_or_404(maestro, id=id)
            serializer = MaestroSerializer(lista_act,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(['Elemento actualizado.'], status=status.HTTP_200_OK)
            else:
                return Response(['Error 400'], status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_503_SERVICE_UNAVAILABLE)

    def delete(self, request, id=None):
        try:
            maestros = maestro.objects.get(id=id)
            maestros.delete()
            return Response(['Elemento eliminado.'], status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_503_SERVICE_UNAVAILABLE)