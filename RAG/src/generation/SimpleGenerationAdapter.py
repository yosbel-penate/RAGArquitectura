from RAG.src.core.IGenerationPort import IGenerationPort
from RAG.src.core.ILanguageModelPort import ILanguageModelPort
from RAG.src.generation.template_formating_promp import load_template_formating_promp

class SimpleGenerationAdapter(IGenerationPort):
    def __init__(self, language_model: ILanguageModelPort, template_formatter):
        self.language_model = language_model
        self.template_formatter = template_formatter

    def generate_response(self, documents: list, query: str) -> str:
        # Implementación de la generación de respuestas
        prompt = f"Query: {query}\nDocuments: {documents}"
        prompt = self.template_formatter(prompt)
        generated_response = self.language_model.generate_text(prompt)
        return generated_response
