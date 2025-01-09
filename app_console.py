import logging
import json

# Configurar logging
logging.basicConfig(level=logging.INFO)

from RAG.src.user.ConsoleDocumentProcessor import ConsoleDocumentProcessor
from RAG.src.vector_store.ChromaVectorStoreAdapter import ChromaVectorStoreAdapter
from RAG.src.output.ConsoleOutputAdapter import ConsoleOutputAdapter


def load_docs_from_json_file():
    with open('chunk_task/chunk.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        documentos = [doc['doc'] for doc in data['docs']]
    return documentos

if __name__ == "__main__":
    vector_store_adapter = ChromaVectorStoreAdapter()
    output_adapter = ConsoleOutputAdapter()

    documentos = load_docs_from_json_file()

    processor = ConsoleDocumentProcessor(vector_store_adapter, documentos, output_adapter=output_adapter)
    processor.process_documents_and_get_answer("dame 1 problema de programacion")
