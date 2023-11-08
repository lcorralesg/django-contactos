# Contactos

Este es un proyecto de Django que simula una página para agregar contactos, con sus respectivos números telefónicos y correos electrónicos, para usarlo se necesita logearse con un usuario y contraseña, si no se tiene uno, se puede crear uno en la página de registro.

## Requisitos

Para poder ejecutar este proyecto, necesitarás tener instalado lo siguiente:

- Python 3 version 3.10.5
- pip
- Una base de datos de tu preferencia (MySQL, PostgreSQL, SQLite, etc.)

## Instalación


1. Abre una terminal en la carpeta raíz del proyecto.
2. Crea un entorno virtual si deseas mantener las dependencias del proyecto aisladas del resto de tu sistema.
    ```
    python -m venv env
    ```
3. Activa el entorno virtual.
    - Windows
        ```
        env\Scripts\activate
        ```
    - Linux
        ```
        source env/bin/activate
        ```
4. Clona este repositorio en tu máquina local o en el servidor host de tu preferencia.
    ```
    git clone https://github.com/Tecsupsoft/lab02-agenda-lcorralesg.git
    ```
5. Ve a la carpeta del proyecto.
    ```
    cd lab02-agenda-lcorralesg
    ```
6. Instala las dependencias del proyecto.
    ```
    pip install -r requirements.txt
    ```
7. Crea un archivo `.env` en la carpeta raíz del proyecto con el siguiente contenido:
    ```
    SECRET_KEY=clave_secreta
    DATABASE_URL=(Cadena de conexión a la base de datos de tu preferencia)
    ```
8. Ejecuta las migraciones.
    ```
    python manage.py migrate
    ```
9. Crea un superusuario.
    ```
    python manage.py createsuperuser
    ```
10. Ejecuta el servidor.
    ```
    python manage.py runserver
    ```
11. Abre un navegador y ve a la dirección `http://localhost:8000/`.

## Deployment en Render y RDS de AWS

1. Crea una cuenta en [Render](https://render.com/).
![Render](https://pbs.twimg.com/media/FbBmoTSWAAAadef.jpg)

2. Crea una base de datos en [AWS RDS](https://aws.amazon.com/rds/).
![AWS RDS](https://cdn.holistics.io/landing/databases/amazon-rds.png)

3. Crea una nueva aplicación en Render.

4. Conecta tu repositorio de GitHub a la aplicación.

5. Ponle un nombre al servicio de la aplicación.

6. Escoje el runtime de Python 3.

7. En el campo de inicio de comando escribe `gunicorn Contactos.wsgi`, Contactos es el nombre del proyecto de Django.

8. Agrega las variables de entorno `SECRET_KEY` que es la clave secreta de Django ubicada en el archivo `settings.py` y `DATABASE_URL` que es la cadena de conexión a la base de datos de AWS RDS (ejemplo: `mysql://usuario:contraseña@host:puerto/nombre_de_la_base_de_datos`), asimismo, agrega la variable de entorno `PYTHON_VERSION` con el valor `3.10.5` para que Render use la versión de Python correcta.

9. Crea el servicio.

10. Espera a que Render termine de construir el servicio.

11. Ve a la dirección de la aplicación.

12. Registrate y logeate.

13. Usa la aplicación.

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/FyOpLM5q)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11747433&assignment_repo_type=AssignmentRepo)