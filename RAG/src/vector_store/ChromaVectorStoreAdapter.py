from chromadb import Client
from chromadb.config import Settings
from RAG.src.core import VectorStorePort

class ChromaVectorStoreAdapter(VectorStorePort):
    def __init__(self):
        self.client = Client(Settings())

    def search_fragments(self, query: str) -> list:
        # Implementación de la búsqueda de fragmentos utilizando Chroma
        results = self.client.query(query)
        return [result['fragment'] for result in results]

    def index_documents(self, documents: list) -> None:
        # Implementación de la indexación de documentos utilizando Chroma
        for doc in documents:
            self.client.index(doc)