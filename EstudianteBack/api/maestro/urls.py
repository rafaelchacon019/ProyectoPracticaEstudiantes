from django.urls import path
from .views import MaestroViews

app_name = 'maestro'

urlpatterns = [
    path('', MaestroViews.as_view()),
    path('<int:id>/', MaestroViews.as_view()),
]