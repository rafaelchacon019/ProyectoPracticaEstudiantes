from django.urls import path
from .views import MaestroViews, MateriasByMaestro

app_name = 'maestro'

urlpatterns = [
    path('', MaestroViews.as_view()),
    path('<int:id>/', MaestroViews.as_view()),
    path('by/<int:id>/', MateriasByMaestro.as_view()),
]