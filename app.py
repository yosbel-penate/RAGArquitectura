import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)

from RAG.src.documents.SimpleDocumentSourceAdapter import SimpleDocumentSourceAdapter
from RAG.src.generation.SimpleGenerationAdapter import SimpleGenerationAdapter
from RAG.src.input.SimpleInputAdapter import SimpleInputAdapter
from RAG.src.output.SimpleOutputAdapter import SimpleOutputAdapter
from RAG.src.retrieval.SimpleRetrievalAdapter import SimpleRetrievalAdapter
from RAG.src.user.ProcessRequestAdapter import ProcessRequestAdapter
from RAG.src.vector_store.ChromaVectorStoreAdapter import ChromaVectorStoreAdapter
from RAG.src.language_model.GeminiLanguageModelAdapter import GeminiLanguageModelAdapter


if __name__ == "__main__":
    vector_store_adapter = ChromaVectorStoreAdapter()

    # Añadir documentos a la colección
    documentos = [
        "París es la capital de Francia.",
        "Berlín es la capital de Alemania.",
        "Madrid es la capital de España."
    ]
    vector_store_adapter.index_documents(documentos)

    adapter = ProcessRequestAdapter(input_adapter = SimpleInputAdapter(),
                            retrieval_adapter = SimpleRetrievalAdapter(vector_store_adapter),
                            generation_adapter = SimpleGenerationAdapter(GeminiLanguageModelAdapter()),
                            output_adapter = SimpleOutputAdapter(),
                            vector_store_adapter = vector_store_adapter,
                            document_source_adapter = SimpleDocumentSourceAdapter())
    adapter.run("¿Cuál es la capital de Estonia?")