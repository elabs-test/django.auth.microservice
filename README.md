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

2. Crea un archivo .env apartir de .env.example en la carpeta raiz del proyecto.

- `POSTGRES_DB`=name_bd
- `POSTGRES_USER`=users_bd
- `POSTGRES_PASSWORD`=password_bd
- `POSTGRES_HOST`=db
- `POSTGRES_PORT`=5432

3. Verifica las dependencias en el archivo requirements.txt:


- asgiref==3.8.1
- Django==5.1.4
- psycopg2-binary==2.9.10
- sqlparse==0.5.3
- tzdata==2024.2
- python-decouple==3.8

+ Asegúrate de que estas dependencias están instaladas en tu contenedor Docker.

4. Construye y ejecuta los contenedores:

``Docker-compose up --build ``

5. Aplica las migraciones de la base de datos:


`docker-compose exec web python manage.py migrate`

-  El servidor estará disponible en http://localhost:8000. 🌐

6. Uso de los Endpoints 🔗

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

- Error 404 en un endpoint: Verifica las rutas configuradas en Users/urls.py.

- Base de datos no conectada: Asegúrate de que las variables en el archivo .env estén correctas.

- Migraciones no aplicadas: Ejecuta docker-compose exec web python manage.py migrate.

