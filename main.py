import os
import json
import time
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

# Define el alcance de la API de Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']
CREDENTIALS_FILE = 'credentials.json'
TOKEN_FILE = 'storage.json'

def authenticate():
    """Autentica y autoriza el acceso a la API de Google Drive."""
    creds = None
    try:
        if os.path.exists(TOKEN_FILE):
            creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
                creds = flow.run_local_server(port=0)
            with open(TOKEN_FILE, 'w') as token:
                token.write(creds.to_json())
    except Exception as e:
        print(f"Error durante la autenticación: {e}")
        raise
    return creds

def create_service():
    """Crea el servicio de Google Drive."""
    try:
        creds = authenticate()
        service = build('drive', 'v3', credentials=creds)
        print("Servicio de Google Drive creado con éxito.")
        return service
    except Exception as e:
        print(f"Error al crear el servicio de Google Drive: {e}")
        raise

def upload_file(filename, filepath, mimetype, folderid):
    """Sube un archivo a Google Drive."""
    try:
        service = create_service()
        file_metadata = {'name': filename, "parents": [folderid]}
        media = MediaFileUpload(filepath, mimetype=mimetype)
        file = service.files().create(
            body=file_metadata, 
            media_body=media, 
            fields='id', 
            supportsAllDrives=True
        ).execute()
        print(f'Archivo subido con éxito. ID del archivo: {file.get("id")}')
    except HttpError as error:
        print(f"Se produjo un error de HTTP: {error}")
    except Exception as e:
        print(f"Ocurrió un error al subir el archivo: {e}")

def create_test_file():
    """Crea un archivo de prueba."""
    test_file_path = 'test_upload.txt'
    try:
        with open(test_file_path, 'w') as f:
            f.write('Este es un archivo de prueba.')
        print("Archivo de prueba creado con éxito.")
    except Exception as e:
        print(f"Error al crear el archivo de prueba: {e}")
        raise
    return test_file_path

if __name__ == '__main__':
    # Reemplaza con el ID de tu carpeta de Google Drive
    folderid = '' 

    # Crea y sube un archivo de prueba
    try:
        test_file_path = create_test_file()
        upload_file('test_upload.txt', test_file_path, 'text/plain', folderid)
    except Exception as e:
        print(f"Error en la ejecución principal: {e}")


    # Ejemplo de cómo usar la función para subir otros archivos
    # filename = 'cible.png'
    # filepath = 'path/to/your/cible.png'
    # mimetype = 'image/png'
    # upload_file(filename, filepath, mimetype, folderid)