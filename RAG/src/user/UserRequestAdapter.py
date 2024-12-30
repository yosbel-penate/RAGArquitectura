from RAG.src.core.IGenerationPort import IGenerationPort
from RAG.src.core.IInputPort import IInputPort
from RAG.src.core.IOutputPort import IOutputPort
from RAG.src.core.IRetrievalPort import IRetrievalPort
from RAG.src.core.IVectorStorePort import IVectorStorePort
from RAG.src.core.IDocumentSourcePort import (
    IDocumentSourcePort)


class UserRequestAdapter:
    def __init__(self, input_adapter: IInputPort,
                retrieval_adapter: IRetrievalPort,
                generation_adapter: IGenerationPort,
                output_adapter: IOutputPort,
                vector_store_adapter: IVectorStorePort,
                document_source_adapter: IDocumentSourcePort):

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