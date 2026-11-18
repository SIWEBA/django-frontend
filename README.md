# SIWEBA - Dashboard & Frontend Layer

Repositorio Frontend de **SIWEBA** (Sistema Web Meteorológico).

Este proyecto contiene la interfaz de usuario, el tablero de control (dashboard) y la capa de presentación desarrollada con **Django** y **Bootstrap** para la visualización e interacción con los módulos de monitoreo meteorológico Arduino.

---

## Stack Tecnológico

* **Framework Principal:** Django 6.1.1 (Motor de Vistas y Templates)
* **Lenguaje Backend Frontend:** Python 3.12+
* **Framework Estilos & UI:** Bootstrap 5.3.8
* **Base de Datos (Desarrollo Local):** SQLite 3 (`db.sqlite3`)
* **Hojas de Estilo:** CSS3 personalizado (`dashboard/static/dashboard/css/estilos.css`)
* **Arquitectura de Interfaz:** Sistema de Herencia de Plantillas (Django Template Engine)

---

## Estructura del Proyecto

    frontend/
    ├── config/                     # Configuración global del proyecto Django (settings, urls, wsgi)
    │   ├── settings.py             # Configuración de base de datos, apps y estáticos
    │   └── urls.py                 # Enrutador principal del sistema
    ├── dashboard/                  # Aplicación principal de la interfaz
    │   ├── static/                 # Archivos estáticos (CSS, JS, imágenes)
    │   │   └── dashboard/css/
    │   │       └── estilos.css     # Estilos personalizados de SIWEBA
    │   ├── templates/              # Plantillas HTML
    │   │   └── dashboard/
    │   │       ├── base.html       # Plantilla maestra (Layout principal con Aside & Header)
    │   │       ├── inicio.html     # Landing page / Inicio público
    │   │       ├── login.html      # Formulario de inicio de sesión
    │   │       ├── registro.html   # Formulario de alta de usuario
    │   │       └── panel.html      # Panel de control de usuario (Dashboard protegido)
    │   ├── admin.py                # Registro de modelos en el panel de admin
    │   ├── models.py               # Modelos de datos locales / representaciones UI
    │   ├── views.py                # Lógica de presentación y autenticación
    │   └── urls.py                 # Rutas internas de la app dashboard
    ├── manage.py                   # Script de gestión de Django
    └── requirements.txt            # Dependencias de Python

---

## Estado de Desarrollo e Implementación

Actualmente el frontend cuenta con los siguientes módulos operativos:

**Layout Base Dinámico (`base.html`):** Barra lateral de navegación adaptativa, cabecera de sesión y contenedor central con el bloque `{% block contenido %}`.
**Módulo de Autenticación de Usuarios:**
  * Registro de usuarios con validación nativa (`UserCreationForm`).
  * Inicio de Sesión seguro (`AuthenticationForm`).
  * Control de acceso a rutas privadas (`@login_required`).
  * Cierre de sesión y estado dinámico en la cabecera.

**Panel de Control Base (`panel.html`):** Vista de bienvenida estilizada para usuarios autenticados.

---

## Instalación y Ejecución Local

Sigue estos pasos para levantar el entorno de desarrollo en tu máquina local:

1. **Clonar el repositorio e ingresar a la carpeta:**

       git clone <URL_DEL_REPOSITORIO_FRONTEND>
       cd frontend

2. **Crear y activar el entorno virtual:**
   * **Windows (PowerShell):**

         python -m venv venv
         .\venv\Scripts\activate

   * **Linux / macOS:**

         python3 -m venv venv
         source venv/bin/activate

3. **Instalar dependencias:**

       pip install -r requirements.txt

4. **Ejecutar migraciones de base de datos:**

       python manage.py migrate

5. **Iniciar el servidor de desarrollo:**

       python manage.py runserver

   El sistema estará disponible en: `http://127.0.0.1:8000/`
