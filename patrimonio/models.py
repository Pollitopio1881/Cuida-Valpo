from django.db import models

class Reporte(models.Model):
    direccion = models.CharField(max_length=255)
    fotos = models.TextField(blank=True, null=True, help_text="Rutas o URLs de las fotos separadas por coma")
    descripcion = models.TextField()

    # Resultados del cuestionario (Booleanos)
    grieta_visible = models.BooleanField(default=False)
    grieta_cambio = models.BooleanField(default=False)
    deformacion = models.BooleanField(default=False)
    desprendimiento = models.BooleanField(default=False)
    filtracion = models.BooleanField(default=False)
    antiguedad = models.BooleanField(default=False)
    zona_patrimonial = models.BooleanField(default=False)

    # Resultados procesados por el sistema
    puntaje = models.IntegerField(default=0)
    nivel_urgencia = models.CharField(
        max_length=10, 
        choices=[("ALTA", "Alta"), ("MEDIA", "Media"), ("BAJA", "Baja")],
        default="BAJA"
    )
    sector = models.CharField(max_length=100, blank=True, null=True)
    tipo_solicitud = models.CharField(
        max_length=20,
        choices=[("INDIVIDUAL", "Individual"), ("AGRUPADA", "Agrupada")],
        default="INDIVIDUAL"
    )
    
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.direccion} - {self.nivel_urgencia}"