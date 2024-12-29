from RAG.src.core.ports import RetrievalPort


class SimpleRetrievalAdapter(RetrievalPort):
    def retrieve_documents(self, query: str) -> list:
        # Implementación de la recuperación de documentos
        return ["doc1", "doc2"]