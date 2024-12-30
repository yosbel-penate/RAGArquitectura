from RAG.src.core.ports import LanguageModelPort
from gemi import GemiClient

class SimpleLanguageModelAdapter(LanguageModelPort):
    def __init__(self):
        self.client = GemiClient()

    def generate_text(self, prompt: str) -> str:
        # Implementación de la generación de texto usando gemi
        response = self.client.generate(prompt)
        return response