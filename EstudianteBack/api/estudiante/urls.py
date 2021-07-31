from django.urls import path
from .views import EstudianteViews

app_name = 'estudiante'

urlpatterns = [
    path('', EstudianteViews.as_view()),
    path('<int:id>/', EstudianteViews.as_view()),
]