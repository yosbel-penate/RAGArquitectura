from RAG.src.documents.SimpleDocumentSourceAdapter import SimpleDocumentSourceAdapter
from RAG.src.generation.SimpleGenerationAdapter import SimpleGenerationAdapter
from RAG.src.input.SimpleInputAdapter import SimpleInputAdapter
from RAG.src.output.SimpleOutputAdapter import SimpleOutputAdapter
from RAG.src.retrieval.SimpleRetrievalAdapter import SimpleRetrievalAdapter
from RAG.src.user.ProcessRequestAdapter import ProcessRequestAdapter
from RAG.src.vector_store.ChromaVectorStoreAdapter import ChromaVectorStoreAdapter
from RAG.src.language_model.GeminiLanguageModelAdapter import (
    GeminiLanguageModelAdapter
)

if __name__ == "__main__":
    adapter = ProcessRequestAdapter(input_adapter = SimpleInputAdapter(),
                            retrieval_adapter = SimpleRetrievalAdapter(),
                            generation_adapter = SimpleGenerationAdapter(GeminiLanguageModelAdapter()),
                            output_adapter = SimpleOutputAdapter(),
                            vector_store_adapter = ChromaVectorStoreAdapter(),
                            document_source_adapter = SimpleDocumentSourceAdapter())
    adapter.run("¿Cuál es la capital de Francia?")