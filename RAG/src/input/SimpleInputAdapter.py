from RAG.src.core.ports import InputPort


class SimpleInputAdapter(InputPort):
    def process_query(self, query: str) -> str:
        # Implementación del preprocesamiento de la consulta
        return query