from django.urls import path
from . import views

urlpatterns = [
    # Cuando alguien entre a la URL principal, Django ejecutará 'formulario_view'
    path('', views.formulario_view, name='formulario'),
]