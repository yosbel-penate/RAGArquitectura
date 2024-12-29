from RAG.src.documents.SimpleDocumentSourceAdapter import SimpleDocumentSourceAdapter
from RAG.src.generation.SimpleGenerationAdapter import SimpleGenerationAdapter
from RAG.src.input.SimpleInputAdapter import SimpleInputAdapter
from RAG.src.output.SimpleOutputAdapter import SimpleOutputAdapter
from RAG.src.retrieval.SimpleRetrievalAdapter import SimpleRetrievalAdapter
from RAG.src.user.ProcessRequestAdapter import ProcessRequestAdapter
from RAG.src.vector_store.SimpleVectorStoreAdapter import SimpleVectorStoreAdapter
from RAG.src.leguage_model.SimpleLanguageModelAdapter import (
    SimpleLanguageModelAdapter
)

if __name__ == "__main__":
    adapter = ProcessRequestAdapter(input_adapter = SimpleInputAdapter(),
                            retrieval_adapter = SimpleRetrievalAdapter(),
                            generation_adapter = SimpleGenerationAdapter(SimpleLanguageModelAdapter()),
                            output_adapter = SimpleOutputAdapter(),
                            vector_store_adapter = SimpleVectorStoreAdapter(),
                            document_source_adapter = SimpleDocumentSourceAdapter())
    adapter.run("¿Cuál es la capital de Francia?")