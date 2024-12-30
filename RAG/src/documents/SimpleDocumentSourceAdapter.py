from RAG.src.core.IDocumentSourcePort import IDocumentSourcePort


class SimpleDocumentSourceAdapter(IDocumentSourcePort):
    def get_documents(self) -> list:
        # Implementación de la obtención de documentos
        return ["doc1", "doc2"]