from RAG.src.core.ports import RetrievalPort
from ..core import VectorStorePort

class SimpleRetrievalAdapter(RetrievalPort):
    def __init__(self, vectorStorePort: VectorStorePort):
        self.vector_store = vectorStorePort()

    def retrieve_documents(self, query: str) -> list:
        # Implementación de la recuperación de documentos
        return self.vector_store.search_fragments(query)