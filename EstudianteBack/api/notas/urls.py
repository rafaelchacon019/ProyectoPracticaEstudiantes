from django.urls import path
from .views import NotasViews

app_name = 'notas'

urlpatterns = [
    path('', NotasViews.as_view()),
    path('<int:id>/', NotasViews.as_view()),
]