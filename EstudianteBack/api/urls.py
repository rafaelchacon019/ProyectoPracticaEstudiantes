from django.urls import path, include

urlpatterns = [
    path('maestro/', include('api.maestro.urls', namespace='maestro')),
    path('estudiante/', include('api.estudiante.urls', namespace='estudiante')),
    path('materias/', include('api.materias.urls', namespace='materias')),
    path('notas/', include('api.notas.urls', namespace='notas')),
]