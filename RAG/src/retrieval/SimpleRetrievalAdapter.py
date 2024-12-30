from RAG.src.core.IRetrievalPort import IRetrievalPort
from ..core import IVectorStorePort

class SimpleRetrievalAdapter(IRetrievalPort):
    def __init__(self, vectorStorePort: IVectorStorePort):
        self.vector_store = vectorStorePort

    def retrieve_documents(self, query: str) -> list:
        # Implementación de la recuperación de documentos
        return self.vector_store.search_fragments(query)