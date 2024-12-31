# Chunk

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
