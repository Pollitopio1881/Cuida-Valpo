# Prediagnóstico Patrimonial

Este proyecto es una aplicación web desarrollada con Django para realizar diagnósticos y gestiones patrimoniales.

---

## Requisitos previos

- Python 3.10 o superior
- Git

---

## Instalación y Configuración

Sigue estos pasos para clonar e instalar el proyecto en tu máquina local:

### 1. Clonar el repositorio
```bash
git clone <URL_DE_TU_REPOSOTORIO>
cd Prediagnostico-patrimonial-main  
```
### 2. Crear admin (hacer una vez)
```bash
python manage.py createsuperuser
```
A continuación va a solicitar crear un nombre de usuario, ingresar un correo y crear una contraseña:
```bash
Username:
Email address:
Password:
Password (again):
Superuser created successfully.
```
Finalmente, para comprobar la instalación correcta se puede dirigir a los siguientes links:

En el primero se deben ingresar las credenciales anteriormente creadas para acceder a las funciones de administración del sitio:
```bash
http://127.0.0.1:8000/admin/
```
El segundo se dirigira al sitio de acceso público:
```bash
http://127.0.0.1:8000/
```
