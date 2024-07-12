# Automatización de Subida de Archivos a Google Drive

Este proyecto proporciona un script en Python para automatizar la subida de archivos a Google Drive utilizando la API de Google Drive.

## Paso a Paso

### 1. Clonar el Repositorio

Para comenzar, clona este repositorio en tu máquina local utilizando Git:


git clone https://github.com/larsai85/upload-file-google-drive.git
cd upload-file-google-drive


### 2. Configurar credentials.json

Para utilizar la API de Google Drive, necesitas configurar las credenciales de OAuth en la Consola de Desarrolladores de Google:

- Visita la Consola de Desarrolladores de Google.
- Crea un nuevo proyecto o selecciona uno existente.
- En el panel de navegación lateral izquierdo, selecciona "Credenciales".
- Haz clic en "Crear credenciales" y selecciona "ID de cliente OAuth".
- Sigue las instrucciones para completar el asistente y descarga el archivo credentials.json.
- Guarda credentials.json en la raíz de tu proyecto clonado (upload-file-google-drive).

### 3. Crear y Activar un Entorno Virtual (Opcional pero recomendado)

python -m venv env
source env/bin/activate  # En Windows usa `env\Scripts\activate`

### 4. Instalar Dependencias

Instala las dependencias necesarias utilizando el archivo requirements.txt:

pip install -r requirements.txt

### 5. Ejecutar el Script

Ejecuta el script principal upload_to_drive.py para subir un archivo de prueba a Google Drive:

python upload_to_drive.py

"# upload-file-google-drive" 
