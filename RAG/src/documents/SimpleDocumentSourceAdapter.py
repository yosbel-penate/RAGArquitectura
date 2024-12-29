from RAG.src.core.ports import DocumentSourcePort


class SimpleDocumentSourceAdapter(DocumentSourcePort):
    def get_documents(self) -> list:
        # Implementación de la obtención de documentos
        return ["doc1", "doc2"]