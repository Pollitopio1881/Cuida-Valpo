# Prediagnóstico Patrimonial

Este proyecto es una aplicación web desarrollada con Django para realizar diagnósticos y guiar e informar a los propietarios sobre que trámites pueden hacer y postular para restaurar sus vivoendas

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
cd Cuida-Valpo-main  
```
### 2. Crear y activar el entorno virtual: 
```bash
python -m venv venv` y luego `.\venv\Scripts\activate`.
```
### 3. Instalar Django: 
```bash
pip install django`.
```
### 4. Crear admin (hacer una vez)
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
### 5.Ejecutar el servidor: 
```bash
python manage.py runserver`.
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
