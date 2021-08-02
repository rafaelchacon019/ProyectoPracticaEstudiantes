from django.urls import path
from .views import EstudianteViews, EstudianteByAll

app_name = 'estudiante'

urlpatterns = [
    path('', EstudianteViews.as_view()),
    path('<int:id>/', EstudianteViews.as_view()),
    path('by/<int:id>/', EstudianteByAll.as_view()),
]