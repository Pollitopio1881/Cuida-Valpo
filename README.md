# CuidaValpo - Proyecto IWG-400 (Grupo 14)
Plataforma web desarrollada en Django para el prediagnóstico patrimonial y arquitectónico en Valparaíso.

## Funcionalidad Principal
Permite a los propietarios evaluar daños estructurales respondiendo un cuestionario. El sistema calcula un nivel de urgencia, entrega un informe con los trámites legales correspondientes (LGUC, Ley 17.288, DS27) y detecta si existen reportes vecinos en el mismo sector para fomentar la postulación comunitaria a evaluaciones profesionales.

## Instrucciones de Ejecución
1. Clonar el repositorio.
2. Crear y activar el entorno virtual: `python -m venv venv` y luego `.\venv\Scripts\activate`.
3. Instalar Django: `pip install django`.
4. Ejecutar el servidor: `python manage.py runserver`.
5. Acceder a `http://127.0.0.1:8000/` en el navegador.

## Panel de Administración
Se puede acceder a `http://127.0.0.1:8000/admin/` con las credenciales creadas localmente mediante `python manage.py createsuperuser` para visualizar los reportes guardados en la base de datos.