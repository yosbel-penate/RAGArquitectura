from RAG.src.core.ports import OutputPort


class SimpleOutputAdapter(OutputPort):
    def present_response(self, response: str) -> None:
        # Implementación de la presentación de la respuesta
        print(response)