# ============================================================
# Prototipo de consola - Registro y pre-diagnóstico de daños
# Grupo 14 - Proyecto IWG400 (viviendas en sectores patrimoniales, Valparaíso)
# Solo usa: input, print, if/else, while, for, listas, diccionarios y funciones.
# ============================================================

# ------------------------------------------------------------
# DATOS INTERNOS
# ------------------------------------------------------------

# Cuestionario: cada pregunta es un diccionario con sus puntos y su fuente.
# OJO: los puntos son una ASUMPCIÓN del equipo hasta completar la fuente.
# "requiere" (opcional): la pregunta solo se hace si esa otra respuesta fue "sí".
# "extra" (opcional): trámite adicional que se agrega si la respuesta es "sí".
PREGUNTAS = [
    {"clave": "grieta_visible", "texto": "¿Hay grietas visibles en muros o fachada?",
     "puntos": 2, "factor": "Grietas visibles", "fuente": "[POR COMPLETAR]"},
    {"clave": "grieta_cambio", "texto": "¿Alguna grieta ha crecido o cambiado en las últimas semanas?",
     "puntos": 3, "factor": "Cambio reciente en grietas", "fuente": "[POR COMPLETAR]",
     "requiere": "grieta_visible"},
    {"clave": "deformacion", "texto": "¿Ves muros inclinados o pisos hundidos?",
     "puntos": 3, "factor": "Deformaciones visibles", "fuente": "[POR COMPLETAR]"},
    {"clave": "desprendimiento", "texto": "¿Se han desprendido trozos de fachada, cornisas o revestimientos?",
     "puntos": 4, "factor": "Desprendimiento de fachada", "fuente": "[POR COMPLETAR]",
     "extra": "zona_patrimonial"},
    {"clave": "filtracion", "texto": "¿Hay filtraciones o manchas de humedad?",
     "puntos": 1, "factor": "Filtraciones o humedad", "fuente": "[POR COMPLETAR]"},
    {"clave": "antiguedad", "texto": "¿La vivienda tiene más de 50 años aproximadamente?",
     "puntos": 1, "factor": "Antigüedad aproximada", "fuente": "[POR COMPLETAR]"},
]

# Trámites posibles, cada uno con su descripción y la fuente que lo respalda.
# Los nombres de las fuentes son los del proyecto; falta verificar artículo y versión vigente.
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

# Qué trámites base corresponden a cada nivel de urgencia.
TRAMITES_POR_NIVEL = {
    "ALTA": ["dom", "profesional", "ds27"],
    "MEDIA": ["profesional", "ds27"],
    "BAJA": ["ds27"],
}

# "Base de datos" simulada: sector -> lista de direcciones ya reportadas.
REPORTES = {
    "alegre": ["Calle Templeman 45, Cerro Alegre"],
    "concepcion": ["Paseo Gervasoni 12, Cerro Concepción"],
    "bellavista": ["Pasaje Bavestrello 8, Cerro Bellavista"],
}


# ------------------------------------------------------------
# FUNCIONES AUXILIARES
# ------------------------------------------------------------

def sin_tildes(texto):
    """Pasa a minúscula y quita tildes para comparar textos."""
    texto = texto.lower()
    cambios = [("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u")]
    for con_tilde, sin_tilde in cambios:
        texto = texto.replace(con_tilde, sin_tilde)
    return texto


def pedir_texto(mensaje):
    """Repite la pregunta hasta que el texto no esté vacío (validación)."""
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("   Este campo es obligatorio.")


def pedir_si_no(mensaje):
    """Devuelve True si el usuario responde 's' y False si responde 'n'."""
    while True:
        respuesta = input(mensaje + " (s/n): ").strip().lower()
        if respuesta == "s":
            return True
        if respuesta == "n":
            return False
        print("   Responde solo con 's' o 'n'.")


def hacer_cuestionario():
    """Hace las preguntas y devuelve un diccionario {clave: True/False}."""
    respuestas = {}
    for pregunta in PREGUNTAS:
        clave = pregunta["clave"]
        if "requiere" in pregunta and not respuestas[pregunta["requiere"]]:
            respuestas[clave] = False
        else:
            respuestas[clave] = pedir_si_no(pregunta["texto"])
    return respuestas


def calcular_urgencia(respuestas):
    """Suma puntos según las respuestas y devuelve (puntaje, nivel, factores)."""
    puntaje = 0
    factores = []
    for pregunta in PREGUNTAS:
        if respuestas[pregunta["clave"]]:
            puntaje = puntaje + pregunta["puntos"]
            factores.append((pregunta["factor"], pregunta["fuente"]))
    if puntaje >= 6:
        nivel = "ALTA"
    elif puntaje >= 3:
        nivel = "MEDIA"
    else:
        nivel = "BAJA"
    return puntaje, nivel, factores


def filtrar_tramites(nivel, respuestas):
    """Devuelve las claves de trámites que corresponden al nivel y a las respuestas."""
    claves = list(TRAMITES_POR_NIVEL[nivel])
    for pregunta in PREGUNTAS:
        if respuestas[pregunta["clave"]] and "extra" in pregunta:
            if pregunta["extra"] not in claves:
                claves.append(pregunta["extra"])
    return claves


def detectar_sector(direccion):
    """Busca en la dirección el nombre de un sector conocido. Devuelve None si no hay."""
    direccion_limpia = sin_tildes(direccion)
    for sector in REPORTES:
        if sector in direccion_limpia:
            return sector
    return None


def buscar_vecinos(direccion, sector):
    """Devuelve las direcciones ya reportadas en el mismo sector (sin la propia)."""
    vecinos = []
    if sector is None:
        return vecinos
    for otra in REPORTES[sector]:
        if sin_tildes(otra) != sin_tildes(direccion):
            vecinos.append(otra)
    return vecinos


def mostrar_ficha(direccion, fotos, descripcion, puntaje, nivel, factores, claves_tramites):
    """Imprime la ficha de pre-diagnóstico orientativo."""
    print("\n" + "=" * 60)
    print("      FICHA DE PRE-DIAGNÓSTICO ORIENTATIVO")
    print("=" * 60)
    print("Dirección:    " + direccion)
    print("Fotos:        " + ", ".join(fotos))
    print("Descripción:  " + descripcion)
    print("Puntaje:      " + str(puntaje))
    print("Nivel de urgencia: " + nivel)
    print("\nFactores considerados:")
    if len(factores) == 0:
        print("  - Ninguno de los daños consultados fue marcado.")
    for factor, fuente in factores:
        print("  - " + factor + "  (fuente: " + fuente + ")")
    print("\nPróximos pasos / trámites:")
    for clave in claves_tramites:
        print("  * " + TRAMITES[clave]["descripcion"])
        print("      Fuente: " + TRAMITES[clave]["fuente"])
    print("\nAviso: esta ficha es orientativa. NO es un diagnóstico estructural.")
    print("=" * 60)


# ------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------------

def main():
    print("=== Registro y pre-diagnóstico de daños ===\n")

    # PASO 1: el propietario ingresa dirección, fotos (simuladas) y responde el cuestionario
    direccion = pedir_texto("Dirección de la vivienda: ")
    texto_fotos = pedir_texto("Fotos (simulado, nombres separados por coma): ")
    fotos = texto_fotos.split(",")
    descripcion = pedir_texto("Describe brevemente el daño: ")
    print("\nResponde lo que puedas observar:")
    respuestas = hacer_cuestionario()

    # PASO 2: el sistema calcula el nivel de urgencia y filtra los trámites
    puntaje, nivel, factores = calcular_urgencia(respuestas)
    claves_tramites = filtrar_tramites(nivel, respuestas)

    # PASO 3: el sistema muestra la ficha de pre-diagnóstico
    mostrar_ficha(direccion, fotos, descripcion, puntaje, nivel, factores, claves_tramites)

    # PASO 4: el sistema busca reportes de vecinos cercanos
    sector = detectar_sector(direccion)
    vecinos = buscar_vecinos(direccion, sector)

    # PASO 5: muestra la opción de agrupación o informa que será individual
    agrupar = False
    if len(vecinos) > 0:
        print("\nHay " + str(len(vecinos)) + " reporte(s) cercano(s):")
        for vecino in vecinos:
            print("  - " + vecino)
        agrupar = pedir_si_no("¿Quieres enviar una solicitud conjunta con ellos?")
    else:
        print("\nNo hay reportes cercanos. La solicitud se mantiene individual.")

    # PASO 6: el usuario confirma, el sistema registra y notifica
    if pedir_si_no("\n¿Confirmas el envío de tu solicitud?"):
        if agrupar:
            tipo = "AGRUPADA"
        else:
            tipo = "INDIVIDUAL"
        if sector is not None:
            REPORTES[sector].append(direccion)
        print("\n>>> NOTIFICACIÓN A ESPECIALISTAS <<<")
        print("Solicitud " + tipo + " registrada.")
        print("Vivienda: " + direccion + " | Urgencia: " + nivel)
        if agrupar:
            print("Viviendas en el grupo: " + str(len(vecinos) + 1))
    else:
        print("\nSolicitud no enviada. No se registró nada.")


main()