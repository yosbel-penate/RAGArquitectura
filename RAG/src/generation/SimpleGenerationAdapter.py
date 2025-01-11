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

        file_names = self.extract_unique_file_names(documents)
        references = self.create_enumerated_references(file_names)
        generated_response += references
        return generated_response

    def create_enumerated_references(self, file_names):
        # Crea la cadena con la lista enumerada de referencias
        references = "\n\nReferences:\n"
        references += "".join(f"{i}. {file_name}\n" for i, file_name in enumerate(file_names, 1))
        return references

    def extract_unique_file_names(self, documents):
        # Extraer nombre de archivos de metadata y eliminar duplicados
        metadata = [doc['metadata'] for doc in documents]
        file_names = list(set(meta['file_name'].replace('.txt', '') for meta in metadata[0]))
        return file_names
