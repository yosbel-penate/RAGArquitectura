from RAG.src.core.IInputPort import IInputPort


class SimpleInputAdapter(IInputPort):
    def process_query(self, query: str) -> str:
        # Implementación del preprocesamiento de la consulta
        return query