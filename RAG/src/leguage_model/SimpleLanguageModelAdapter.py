from RAG.src.core.ports import LanguageModelPort


class SimpleLanguageModelAdapter(LanguageModelPort):
    def generate_text(self, prompt: str) -> str:
        # Implementación de la generación de texto
        return "Generated response based on prompt"