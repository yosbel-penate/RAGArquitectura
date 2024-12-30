from RAG.src.core.IOutputPort import IOutputPort


class ConsoleOutputAdapter(IOutputPort):
    def present_response(self, response: str) -> None:
        # Implementación de la presentación de la respuesta
        print(response)