from chromadb import Client
from chromadb.config import Settings
from ..core import VectorStorePort

class ChromaVectorStoreAdapter(VectorStorePort):
    def __init__(self):
        self.client = Client(Settings())

    def search_fragments(self, query: str) -> list:
        # Implementación de la búsqueda de fragmentos utilizando Chroma
        results = self.client.query(query_texts=[query])
        return [result['documents'] for result in results]

    def index_documents(self, documents: list) -> None:
        # Implementación de la indexación de documentos utilizando Chroma
        self.client.index(documents=documents)