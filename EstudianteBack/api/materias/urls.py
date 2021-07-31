from django.urls import path
from .views import MateriasViews

app_name = 'materias'

urlpatterns = [
    path('', MateriasViews.as_view()),
    path('<int:id>/', MateriasViews.as_view()),
]