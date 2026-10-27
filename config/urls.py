from django.contrib import admin
from django.urls import path, include  # <-- Asegúrate de importar 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    # Esto delega todo el tráfico inicial a las rutas de tu app patrimonio
    path('', include('patrimonio.urls')), 
]