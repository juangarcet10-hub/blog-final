# Blog Final - Django

## Descripción del proyecto

Aplicación web tipo blog desarrollada con Django como proyecto final del curso de Python. Permite a los usuarios registrarse, iniciar sesión, y crear/gestionar sus propias publicaciones (posts). Incluye panel de administración, formularios con validación, y navegación entre páginas.

**Problema que resuelve:** Ofrece una plataforma simple para que cualquier usuario registrado pueda publicar contenido propio (artículos, notas, entradas de blog) sin necesidad de conocimientos técnicos.

**Usuario objetivo:** Personas que quieran compartir contenido escrito de forma sencilla, sin necesidad de plataformas complejas.

## Funcionalidades principales

- **Panel de administración**: gestión de posts y usuarios desde `/admin`
- **Registro y autenticación de usuarios**: los usuarios pueden crear una cuenta, iniciar sesión y cerrar sesión
- **Perfil de usuario**: cada usuario puede ver y editar su información (bio)
- **Listado y detalle de posts**: navegación entre todas las publicaciones y vista individual de cada una
- **Creación y edición de posts**: formularios con validación para usuarios autenticados (solo el autor puede editar su propio post)
- **Interfaz con Bootstrap**: navegación dinámica según el estado de sesión del usuario

## Requisitos previos

- Python 3.10 o superior
- pip
- Git

## Instalación y ejecución local

1. Cloná el repositorio:
git clone https://github.com/juangarcet10-hub/blog-final.git
cd blog-final

2. Creá y activá un entorno virtual:
python -m venv venv
venv\scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

3. Instalá las dependencias:
pip install -r requirements.txt

4. Aplicá las migraciones:
python manage.py migrate

5. Creá un superusuario (opcional, para acceder al admin):
python manage.py createsuperuser

6. Corré el servidor:
python manage.py runserver

7. Abrí en el navegador:
http://127.0.0.1:8000/

## Despliegue

- **URL pública**: https://blog-final-s76m.onrender.com
- **Entorno de despliegue**: Render (Web Service, plan gratuito)
- **Detalles técnicos**: la aplicación usa gunicorn como servidor WSGI de producción y whitenoise para servir los archivos estáticos. Las variables SECRET_KEY y DEBUG se configuran como variables de entorno en Render, no quedan expuestas en el código.

## Estructura del proyecto

blog-final/
├── blogproject/       # Configuración principal de Django
├── posts/              # App principal: modelos, vistas, templates
│   ├── migrations/
│   ├── templates/posts/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
├── build.sh            # Script de build para Render
├── manage.py
├── requirements.txt
└── README.md

## Autor

Juan - Proyecto final Django, Coderhouse