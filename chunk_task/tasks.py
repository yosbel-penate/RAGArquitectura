import chromadb
from chromadb.config import Settings

# Configuración de la base de datos Chromadb
client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="./chromadb"))

def fragment_text(text):
    """
    Fragmenta el texto en fragmentos de tamaño fijo.

    :param text: Texto a fragmentar
    :return: Lista de fragmentos de texto
    """
    fragment_size = 100  # Tamaño del fragmento
    fragments = [text[i:i + fragment_size] for i in range(0, len(text), fragment_size)]
    return fragments

def process_file(file_path):
    """
    Procesa el archivo, fragmenta su contenido y guarda los fragmentos en la base de datos.

    :param file_path: Ruta del archivo a procesar
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    fragments = fragment_text(data)
    collection = client.get_or_create_collection("text_fragments")
    for index, fragment in enumerate(fragments):
        collection.add({
            "file_path": file_path,
            "fragment_index": index,
            "fragment": fragment
        })
    print(f"Archivo procesado y fragmentado: {file_path}")
