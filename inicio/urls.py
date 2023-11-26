from django.urls import path
from . import views
from .views import Inicio

app_name = 'inicio'

urlpatterns = [
    path('', views.index, name='inicio'),
]
