import logging
import json
import os

# Configurar logging
logging.basicConfig(level=logging.INFO)

from RAG.src.user.ConsoleDocumentProcessor import ConsoleDocumentProcessor
from RAG.src.vector_store.ChromaVectorStoreAdapter import ChromaVectorStoreAdapter
from RAG.src.output.ConsoleOutputAdapter import ConsoleOutputAdapter
from tools import load_docs_from_json_file


if __name__ == "__main__":
    persist_directory = os.path.join(os.path.dirname(__file__), 'vectorDB')

    documentos=[]
    if not os.path.exists(persist_directory):
        os.makedirs(persist_directory)
        documentos = load_docs_from_json_file()

    vector_store_adapter = ChromaVectorStoreAdapter(persist_directory=persist_directory)
    output_adapter = ConsoleOutputAdapter()


    processor = ConsoleDocumentProcessor(vector_store_adapter, documentos, output_adapter=output_adapter)
    processor.process_documents_and_get_answer("dame 1 problema de programacion")
