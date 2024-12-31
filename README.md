# Indice

1. Documentación de la API.
2. Instalar y correr el Chunk Task.
3. Bot de Telegram.


# Documentación de la API

## Instalación

1. Clona el repositorio:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd RAGArquitectura
    ```

2. Crea un entorno virtual y actívalo:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Inicia la aplicación Flask:
    ```bash
    python app_api.py
    ```

2. La API estará disponible en `http://127.0.0.1:5000`.

## Endpoints

### Agregar Documentos

- **URL:** `/add_documents`
- **Método:** `POST`
- **Descripción:** Agrega documentos al vector store.
- **Cuerpo de la solicitud:**
    ```json
    {
        "documents": ["Documento 1", "Documento 2"]
    }
    ```
- **Respuesta exitosa:**
    ```json
    {
        "status": "success"
    }
    ```

### Buscar Fragmentos

- **URL:** `/search`
- **Método:** `GET`
- **Descripción:** Busca fragmentos en el vector store.
- **Parámetros de consulta:**
    - `query`: La consulta de búsqueda.
- **Respuesta exitosa:**
    ```json
    {
        "results": ["Fragmento 1", "Fragmento 2"]
    }
    ```

### Generar Respuesta

- **URL:** `/generate_answer`
- **Método:** `POST`
- **Descripción:** Genera una respuesta basada en una consulta.
- **Cuerpo de la solicitud:**
    ```json
    {
        "query": "Tu consulta aquí"
    }
    ```
- **Respuesta exitosa:**
    ```json
    {
        "answer": "Respuesta generada"
    }
    ```

### Obtener Documento por ID

- **URL:** `/get_document/<doc_id>`
- **Método:** `GET`
- **Descripción:** Obtiene un documento por su ID.
- **Respuesta exitosa:**
    ```json
    {
        "document": "Contenido del documento"
    }
    ```

### Eliminar Documento por ID

- **URL:** `/delete_document/<doc_id>`
- **Método:** `DELETE`
- **Descripción:** Elimina un documento por su ID.
- **Respuesta exitosa:**
    ```json
    {
        "status": "success"
    }
    ```

# Instalar y correr el Chunk Task
## Chunk

Este proyecto monitorea una carpeta para nuevos archivos de texto, los fragmenta y guarda los fragmentos en una base de datos Chromadb local utilizando Redis Queue (RQ).

## Requisitos

- Python 3.x
- Redis

## Instalación

1. Clona este repositorio.
2. Navega al directorio del proyecto.
3. Ejecuta `pip install -r requirements.txt` para instalar las dependencias.

## Uso

1. Inicia un servidor Redis.
2. Ejecuta el trabajador de RQ con el comando `python worker.py`.
3. Ejecuta el script de monitoreo con el comando `python monitor.py`.

Asegúrate de cambiar la ruta de la carpeta a monitorear en el archivo `monitor.py` en la línea:

```python
DIRECTORY_TO_WATCH = "/path/to/monitor"
```


# Bot de Telegram

Este es un bot de Telegram que responde a preguntas enviadas por los usuarios.

## Instalación

1. Clona el repositorio:
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd RAGArquitectura
    ```

2. Crea un entorno virtual y actívalo:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Configura la variable de entorno `TELEGRAM_TOKEN` con el token de tu bot de Telegram:
    ```sh
    export TELEGRAM_TOKEN=<TU_TELEGRAM_TOKEN>  # En Windows usa `set TELEGRAM_TOKEN=<TU_TELEGRAM_TOKEN>`
    ```

## Uso

1. Inicia el servidor Flask:
    ```sh
    flask run
    ```

2. Inicia el bot de Telegram:
    ```sh
    python telegram_bot.py
    ```

3. Abre Telegram y busca tu bot. Envíale el comando `/start` para comenzar a interactuar con él.

## Estructura del Proyecto

- `telegram_bot.py`: Contiene la lógica del bot de Telegram.
- `requirements.txt`: Lista de dependencias necesarias para ejecutar el proyecto.

## Notas

- Asegúrate de que el servidor Flask esté corriendo en `http://localhost:5000` o ajusta la variable `API_URL` en `telegram_bot.py` según sea necesario.