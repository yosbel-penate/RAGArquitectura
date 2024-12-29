from RAG.src.core.ports import GenerationPort, LanguageModelPort


class SimpleGenerationAdapter(GenerationPort):
    def __init__(self, language_model: LanguageModelPort):
        self.language_model = language_model

    def generate_response(self, documents: list, query: str) -> str:
        # Implementación de la generación de respuestas
        prompt = f"Query: {query}\nDocuments: {documents}"
        return self.language_model.generate_text(prompt)