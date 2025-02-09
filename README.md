# Microservicio de Autenticación

Este es un microservicio de autenticación desarrollado en Django. Proporciona funcionalidades de registro,inicio de sesión y recuperación de contraseña.

---

## ✨ Características

- Registro de usuarios con validación de contraseña.
- Inicio de sesión con credenciales seguras.
- Recuperación de contraseña.
- Integrado con Docker para un despliegue rápido y sencillo.
  
---

## 🚀 Tecnologías Utilizadas

- **Python 3.10**
- **Django 5.1.4**
- **PostgreSQL 15**
- **Docker & Docker Compose**

---

## ⚙️ Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

### 🛠️ Requisitos Previos

- Git
- Docker y Docker Compose

### 📋 Pasos

1. Clona el repositorio.

2. Crea un archivo .env basado en el archivo .env.example ubicado en la carpeta raíz del proyecto,edita el archivo .env para incluir la configuración necesaria. A continuación, se muestra un ejemplo con los valores predeterminados:

- DEBUG=1
- DB_NAME=auth_db
- DB_USER=postgres
- DB_PASSWORD=adminpass
- DB_HOST=db
- DB_PORT=5432

1. Verifica las dependencias en el archivo requirements.txt:

- asgiref==3.8.1
- Django==5.1.4
- psycopg2-binary==2.9.10
- sqlparse==0.5.3
- tzdata==2024.2
- python-decouple==3.8

4. Construye y ejecuta los contenedores:

``docker-compose up 

-  El servidor estará disponible en http://localhost:8000. 🌐

1. Uso de los Endpoints 🔗

Registro de Usuario 📝

Endpoint: /auth/register/
Método: POST
Body:

{
  "username": "nombre_usuario",
  "email": "correo@example.com",
  "password": "ContraseñaSegura!"
}

Inicio de Sesión 🔑

Endpoint: /auth/login/
Método: POST
Body:

{
  "email": "correo@example.com",
  "password": "pasword!"
}

Recuperación de Contraseña ✉️

Endpoint: /auth/recovery-password/
Método: POST
Body:

{
  "email": "correo@example.com"
}
 
7. Ejecución de Pruebas 🧪

* El proyecto incluye pruebas automatizadas para validar la funcionalidad:

Ejecuta todas las pruebas:

- `docker-compose exec web python manage.py test`

 Solución de Problemas 🛠️

- Error 404 en un endpoint: Verifica las rutas configuradas en users/urls.py.

- Base de datos no conectada: Asegúrate de que las variables en el archivo .env estén correctas.

- Migraciones no aplicadas: Ejecuta docker-compose exec web python manage.py migrate.

