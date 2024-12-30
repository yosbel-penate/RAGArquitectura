from RAG.src.documents.SimpleDocumentSourceAdapter import SimpleDocumentSourceAdapter
from RAG.src.generation.SimpleGenerationAdapter import SimpleGenerationAdapter
from RAG.src.input.SimpleInputAdapter import SimpleInputAdapter
from RAG.src.language_model.GeminiLanguageModelAdapter import GeminiLanguageModelAdapter

from RAG.src.retrieval.SimpleRetrievalAdapter import SimpleRetrievalAdapter
from RAG.src.user.UserRequestAdapter import UserRequestAdapter
from RAG.src.core.IVectorStorePort import IVectorStorePort
from RAG.src.core.IOutputPort import IOutputPort


class ConsoleDocumentProcessor:
    def __init__(self, vector_store_adapter:IVectorStorePort, documentos:list, output_adapter:IOutputPort):
        self.vector_store_adapter = vector_store_adapter
        self.documentos = documentos
        self.output_adapter=output_adapter

    def process_documents_and_get_answer(self, query:str):
        self.vector_store_adapter.index_documents(self.documentos)

        adapter = UserRequestAdapter(input_adapter=SimpleInputAdapter(),
                                        retrieval_adapter=SimpleRetrievalAdapter(self.vector_store_adapter),
                                        generation_adapter=SimpleGenerationAdapter(GeminiLanguageModelAdapter()),
                                        output_adapter=self.output_adapter,
                                        vector_store_adapter=self.vector_store_adapter,
                                        document_source_adapter=SimpleDocumentSourceAdapter())
        adapter.run(query)