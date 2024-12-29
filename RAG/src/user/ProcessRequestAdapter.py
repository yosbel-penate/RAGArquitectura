from RAG.src.core.ports import (
    DocumentSourcePort, GenerationPort,
    InputPort, OutputPort,
    RetrievalPort, VectorStorePort)


class ProcessRequestAdapter:
    def __init__(self, input_adapter: InputPort,
                retrieval_adapter: RetrievalPort,
                generation_adapter: GenerationPort,
                output_adapter: OutputPort,
                vector_store_adapter: VectorStorePort,
                document_source_adapter: DocumentSourcePort):

        self.input_adapter = input_adapter
        self.retrieval_adapter = retrieval_adapter
        self.generation_adapter = generation_adapter
        self.output_adapter = output_adapter
        self.vector_store_adapter = vector_store_adapter
        self.document_source_adapter = document_source_adapter

    def run(self, query: str):
        processed_query = self.input_adapter.process_query(query)
        documents = self.retrieval_adapter.retrieve_documents(processed_query)
        response = self.generation_adapter.generate_response(documents, processed_query)
        self.output_adapter.present_response(response)