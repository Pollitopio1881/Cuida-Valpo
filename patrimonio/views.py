from django.shortcuts import render
from .models import Reporte

def formulario_view(request):
    # 1. Si el usuario hace clic en "Enviar" en la página, el método es POST
    if request.method == 'POST':
        
        # A. RECIBIR DATOS (Reemplaza a los input() de tu script)
        # Extraemos lo que el usuario escribió usando el 'name' del formulario HTML
        dir_ingresada = request.POST.get('direccion')
        desc_ingresada = request.POST.get('descripcion')
        
        # Para los booleanos (checkboxes del HTML), si están marcados llegan como 'on'
        grieta_vis = request.POST.get('grieta_visible') == 'on'
        deformacion_vis = request.POST.get('deformacion') == 'on'
        # (Aquí debes agregar el resto de tus variables del cuestionario)

        # B. TU LÓGICA DE NEGOCIO (Reemplaza a calcular_urgencia)
        # Aquí sumas los puntos exactamente como lo hacías en consola
        puntaje_total = 0
        if grieta_vis:
            puntaje_total += 2
        if deformacion_vis:
            puntaje_total += 3
        # (Completa la suma de puntos)

        # Determinar nivel
        if puntaje_total >= 6:
            nivel = "ALTA"
        elif puntaje_total >= 3:
            nivel = "MEDIA"
        else:
            nivel = "BAJA"

        # C. GUARDAR EN LA BASE DE DATOS
        nuevo_reporte = Reporte.objects.create(
            direccion=dir_ingresada,
            descripcion=desc_ingresada,
            grieta_visible=grieta_vis,
            deformacion=deformacion_vis,
            puntaje=puntaje_total,
            nivel_urgencia=nivel
            # (Agrega los demás campos que falten)
        )

        # D. SERVIR EL RESULTADO (Reemplaza a los print() de tu ficha)
        # Le pasamos las variables al archivo resultado.html para que las muestre
        contexto = {
            'reporte': nuevo_reporte,
            'nivel': nivel,
            'puntaje': puntaje_total
        }
        return render(request, 'patrimonio/resultado.html', contexto)

    # 2. Si el usuario recién entra a la página (método GET), le mostramos el formulario vacío
    return render(request, 'patrimonio/formulario.html')
