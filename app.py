import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)

from RAG.src.user.ConsoleDocumentProcessor import ConsoleDocumentProcessor
from RAG.src.vector_store.ChromaVectorStoreAdapter import ChromaVectorStoreAdapter


if __name__ == "__main__":
    vector_store_adapter = ChromaVectorStoreAdapter()

    # Añadir documentos a la colección
    documentos = [
        "París es la capital de Francia.",
        "Berlín es la capital de Alemania.",
        "Madrid es la capital de España."
    ]
    processor = ConsoleDocumentProcessor(vector_store_adapter, documentos)
    processor.process_documents()
