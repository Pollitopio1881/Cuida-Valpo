from django.shortcuts import render
from .models import Reporte

def formulario_view(request):
    if request.method == 'POST':
        # Extraer datos del formulario HTML
        dir_ingresada = request.POST.get('direccion')
        desc_ingresada = request.POST.get('descripcion')
        
        grieta_vis = request.POST.get('grieta_visible') == 'on'
        grieta_cambio_vis = request.POST.get('grieta_cambio') == 'on'
        deformacion_vis = request.POST.get('deformacion') == 'on'
        desprendimiento_vis = request.POST.get('desprendimiento') == 'on'
        filtracion_vis = request.POST.get('filtracion') == 'on'
        antiguedad_vis = request.POST.get('antiguedad') == 'on'
        zona_patrimonial_vis = request.POST.get('zona_patrimonial') == 'on'

        # Sumar puntaje
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

        # Guardar en base de datos
        nuevo_reporte = Reporte.objects.create(
            direccion=dir_ingresada,
            descripcion=desc_ingresada,
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

        # Enviar al HTML de resultados
        contexto = {
            'reporte': nuevo_reporte,
            'nivel': nivel,
            'puntaje': puntaje_total
        }
        return render(request, 'patrimonio/resultado.html', contexto)

    return render(request, 'patrimonio/formulario.html')