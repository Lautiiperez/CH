# Clínica Médica

## Descripción General

La Clínica Médica es una plataforma web desarrollada con Django que permite a los usuarios gestionar citas médicas, consultas y seguimientos. Ofrece funcionalidades para administradores, médicos y pacientes, facilitando la comunicación y el acceso a servicios de salud.

## Características Principales

- Gestión de citas médicas.
- Consultas y seguimientos de pacientes.
- Sistema de autenticación y autorización para diferentes roles (administrador, médico, paciente).


## Requisitos

### Dependencias

- Python 3.8+
- Django 3.2+
- PostgreSQL (preferiblemente)

### Software Requerido

- Git para clonar el repositorio.
- Un servidor web para desplegar la aplicación (por ejemplo, Apache, Nginx).

## Instalación

### Clonar Repositorio

1. Clona el repositorio en tu máquina local usando Git:

   ```
   git clone https://github.com/Lautiiperez/CH/tree/main/Python/ProyectoFinal/ClinicaMedica.git
   cd ClinicaMedica
   ```

### Configuración del Entorno

1. Crea un entorno virtual para Python:

   ```
   python -m venv venv
   ```

2. Activa el entorno virtual:

   - En Windows:
     ```
     .\venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```
     source venv/bin/activate
     ```

3. Instala las dependencias del proyecto:

   ```
   pip install -r requirements.txt
   ```

### Configuración de la Base de Datos

1. Configura tu base de datos PostgreSQL y asegúrate de tener la cadena de conexión correcta en tu archivo `settings.py`.

2. Ejecuta las migraciones de Django:

   ```
   python manage.py migrate
   ```

### Variables de Entorno

- Define las variables de entorno necesarias en un archivo `.env` o en tu sistema operativo, como la clave secreta de Django y cualquier otra configuración sensible.

## Uso

### Ejecución Local

1. Inicia el servidor de desarrollo de Django:

   ```
   python manage.py runserver
   ```

2. Accede al proyecto en tu navegador web en `http://localhost:8000`.

### Pruebas Unitarias

- Ejecuta las pruebas unitarias con:

   ```
   python manage.py test
   ```

### Contribuciones

- Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request con tus cambios.

## Licencia

- El proyecto está licenciado bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

