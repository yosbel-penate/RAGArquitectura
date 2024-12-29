from RAG.src.core.ports import VectorStorePort


class SimpleVectorStoreAdapter(VectorStorePort):
    def search_fragments(self, query: str) -> list:
        # Implementación de la búsqueda de fragmentos
        return ["fragment1", "fragment2"]

    def index_documents(self, documents: list) -> None:
        # Implementación de la indexación de documentos
        pass