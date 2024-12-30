from chromadb import Client
from chromadb.config import Settings

from RAG.src.core.IVectorStorePort import IVectorStorePort


class ChromaVectorStoreAdapter(IVectorStorePort):
    def __init__(self):
        self.client = Client(Settings())
        self.collection_name = "mi_coleccion"
        self.collection = self.client.get_or_create_collection(name = self.collection_name)

    def search_fragments(self, query: str) -> list:
        # Implementación de la búsqueda de fragmentos utilizando Chroma
        results = self.collection.query(query_texts=[query])
        if "documents" in results:
            return results['documents']
        else:
            return [result['documents'] for result in results['results']]

    def index_documents(self, documents: list) -> None:
        # Implementación de la indexación de documentos utilizando Chroma
        if not documents:
            raise ValueError("La lista de textos no puede estar vacía.")
        ids = [str(i) for i in range(len(documents))]
        self.collection.add(documents=documents, ids=ids)