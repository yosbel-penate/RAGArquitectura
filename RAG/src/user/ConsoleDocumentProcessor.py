from RAG.src.documents.SimpleDocumentSourceAdapter import SimpleDocumentSourceAdapter
from RAG.src.generation.SimpleGenerationAdapter import SimpleGenerationAdapter
from RAG.src.input.SimpleInputAdapter import SimpleInputAdapter
from RAG.src.language_model.GeminiLanguageModelAdapter import GeminiLanguageModelAdapter
from RAG.src.output.SimpleOutputAdapter import SimpleOutputAdapter
from RAG.src.retrieval.SimpleRetrievalAdapter import SimpleRetrievalAdapter
from RAG.src.user.UserRequestAdapter import UserRequestAdapter


class ConsoleDocumentProcessor:
    def __init__(self, vector_store_adapter, documentos):
        self.vector_store_adapter = vector_store_adapter
        self.documentos = documentos

    def process_documents(self):
        self.vector_store_adapter.index_documents(self.documentos)

        adapter = UserRequestAdapter(input_adapter=SimpleInputAdapter(),
                                        retrieval_adapter=SimpleRetrievalAdapter(self.vector_store_adapter),
                                        generation_adapter=SimpleGenerationAdapter(GeminiLanguageModelAdapter()),
                                        output_adapter=SimpleOutputAdapter(),
                                        vector_store_adapter=self.vector_store_adapter,
                                        document_source_adapter=SimpleDocumentSourceAdapter())
        adapter.run("¿Cuál es la capital de Alemania?")