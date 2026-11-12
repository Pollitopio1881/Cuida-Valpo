Markdown
# 🏛️ CuidaValpo - Prediagnóstico Patrimonial y Acción Comunitaria

Plataforma web desarrollada en **Django** para el curso IWG-400 (Grupo 14). Permite a propietarios y vecinos de Valparaíso evaluar daños estructurales en viviendas antiguas, recibir orientación sobre trámites legales vigentes y visualizar reportes cercanos para fomentar postulaciones conjuntas a evaluaciones técnicas.

## Funcionalidades Principales
* **Formulario Georreferenciado:** Mapa interactivo integrado con **Leaflet.js** y consumo de la **API pública de Nominatim (OpenStreetMap)** para autocompletar direcciones mediante geocodificación inversa.
* **Motor de Orientación Normativa:** Cálculo automático del nivel de urgencia (`ALTA`, `MEDIA`, `BAJA`) y filtrado de trámites legales asociados (LGUC, OGUC, DS27 MINVU y Ley 17.288 de Monumentos Nacionales).
* **Agrupación Vecinal Inteligente:** Detección de reportes activos en el mismo sector, filtrando direcciones duplicadas para evitar falsos conteos.
* **Dashboard Comunitario (`/comunidad/`):** Vista consolidada con historial de reportes persistidos en la base de datos para coordinar acciones entre vecinos.

## Instalación y Ejecución Local

1.**Clonar el repositorio:**
-----------------------------------------------------
    git clone [https://github.com/Pollitopio1881/Proyecto-Inicial-IWG400.git](https://github.com/Pollitopio1881/Proyecto-Inicial-IWG400.git)
-----------------------------------------------------
    cd Cuida-Valpo-main

2.Crear y activar el entorno virtual:

En Windows (PowerShell):
-----------------------------------------------------
    python -m venv venv
    .\venv\Scripts\activate
-----------------------------------------------------
En Linux/Mac:
-----------------------------------------------------
    python3 -m venv venv
    source venv/bin/activate
-----------------------------------------------------
3.Instalar dependencias:

    pip install -r requirements.txt
-----------------------------------------------------
4.Preparar la base de datos y cargar datos de demostración:
-----------------------------------------------------
    python manage.py migrate  
-----------------------------------------------------
    python manage.py loaddata datos_demo.json
-----------------------------------------------------
5.Crear superusuario (Para acceder al Panel de Administración):
-----------------------------------------------------
    python manage.py createsuperuser
-----------------------------------------------------
6.Iniciar el servidor:
-----------------------------------------------------
    python manage.py runserver
-----------------------------------------------------
Rutas del Sistema
Formulario principal: http://127.0.0.1:8000/

Panel comunitario: http://127.0.0.1:8000/comunidad/

Administración Django: http://127.0.0.1:8000/admin/

Equipo (Grupo 14)

-Richard Jiménez

-Martín Fischer

-Álvaro Zenteno

-Emily Jiménez

-Gaspar Bahamondes