from django.shortcuts import render
from .models import Reporte

TRAMITES = {
    "dom": {
        "descripcion": "Consultar a la DOM de Valparaíso si la reparación requiere permiso o inspección",
        "fuente": "Ley General de Urbanismo y Construcciones / Guía DOM [VERIFICAR artículo]",
    },
    "profesional": {
        "descripcion": "Solicitar evaluación de un arquitecto o ingeniero civil",
        "fuente": "[POR COMPLETAR]",
    },
    "ds27": {
        "descripcion": "Revisar si puedes postular al programa de mejoramiento de viviendas DS27",
        "fuente": "DS27 MINVU [VERIFICAR requisitos vigentes]",
    },
    "zona_patrimonial": {
        "descripcion": "Si la vivienda está en zona protegida, consultar antes de intervenir la fachada",
        "fuente": "Ley 17.288 de Monumentos Nacionales [VERIFICAR si aplica a tu sector]",
    },
}

TRAMITES_POR_NIVEL = {
    "ALTA": ["dom", "profesional", "ds27"],
    "MEDIA": ["profesional", "ds27"],
    "BAJA": ["ds27"],
}

SECTORES = [
    ("Cerro Alegre", "Cerro Alegre"),
    ("Cerro Concepción", "Cerro Concepción"),
    ("Cerro Bellavista", "Cerro Bellavista"),
]

def formulario_view(request):
    if request.method == 'POST':
        dir_ingresada = request.POST.get('direccion')
        desc_ingresada = request.POST.get('descripcion')
        sector_ingresado = request.POST.get('sector')
        
        lat_ingresada = request.POST.get('latitud')
        lon_ingresada = request.POST.get('longitud')
        lat_val = float(lat_ingresada) if lat_ingresada else None
        lon_val = float(lon_ingresada) if lon_ingresada else None
        
        grieta_vis = request.POST.get('grieta_visible') == 'on'
        grieta_cambio_vis = request.POST.get('grieta_cambio') == 'on'
        deformacion_vis = request.POST.get('deformacion') == 'on'
        desprendimiento_vis = request.POST.get('desprendimiento') == 'on'
        filtracion_vis = request.POST.get('filtracion') == 'on'
        antiguedad_vis = request.POST.get('antiguedad') == 'on'
        zona_patrimonial_vis = request.POST.get('zona_patrimonial') == 'on'

        puntaje_total = 0
        if grieta_vis: puntaje_total += 2
        if grieta_cambio_vis: puntaje_total += 3
        if deformacion_vis: puntaje_total += 3
        if desprendimiento_vis: puntaje_total += 4
        if filtracion_vis: puntaje_total += 1
        if antiguedad_vis: puntaje_total += 1

        if puntaje_total >= 6:
            nivel = "ALTA"
        elif puntaje_total >= 3:
            nivel = "MEDIA"
        else:
            nivel = "BAJA"

        nuevo_reporte = Reporte.objects.create(
            direccion=dir_ingresada,
            descripcion=desc_ingresada,
            sector=sector_ingresado,
            latitud=lat_val,
            longitud=lon_val,
            grieta_visible=grieta_vis,
            grieta_cambio=grieta_cambio_vis,
            deformacion=deformacion_vis,
            desprendimiento=desprendimiento_vis,
            filtracion=filtracion_vis,
            antiguedad=antiguedad_vis,
            zona_patrimonial=zona_patrimonial_vis,
            puntaje=puntaje_total,
            nivel_urgencia=nivel
        )

        claves_tramites = list(TRAMITES_POR_NIVEL[nivel])
        if zona_patrimonial_vis and "zona_patrimonial" not in claves_tramites:
            claves_tramites.append("zona_patrimonial")

        tramites_recomendados = []
        for clave in claves_tramites:
            tramites_recomendados.append(TRAMITES[clave])

        vecinos_count = Reporte.objects.filter(sector=sector_ingresado).exclude(id=nuevo_reporte.id).count()

        contexto = {
            'reporte': nuevo_reporte,
            'nivel': nivel,
            'puntaje': puntaje_total,
            'tramites': tramites_recomendados,
            'reportes_cercanos': vecinos_count,
        }
        return render(request, 'patrimonio/resultado.html', contexto)

    return render(request, 'patrimonio/formulario.html', {'sectores': SECTORES})