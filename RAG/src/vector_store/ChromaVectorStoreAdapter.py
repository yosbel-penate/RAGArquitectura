from chromadb import Client
from chromadb.config import Settings

from RAG.src.core.IVectorStorePort import IVectorStorePort


class ChromaVectorStoreAdapter(IVectorStorePort):
    def __init__(self, persist_directory):
        self.client = Client(Settings(persist_directory=persist_directory))
        self.collection_name = "mi_coleccion"
        self.collection = self.client.get_or_create_collection(name=self.collection_name)

    def search_fragments(self, query: str) -> list:
        # Implementación de la búsqueda de fragmentos utilizando Chroma
        results = self.collection.query(query_texts=[query])
        if "documents" in results:
            return [{"document": doc, "metadata": meta} for doc, meta in zip(results['documents'], results['metadatas'])]
        else:
            return [{"document": result['documents'], "metadata": result['metadatas']} for result in results['results']]

    def index_documents(self, documents: list) -> None:
        # Implementación de la indexación de documentos utilizando Chroma
        if documents:
            ids = [str(i) for i in range(len(documents))]
            docs_to_index = [doc["doc"]["doc"] for doc in documents]
            metadata_to_index = [doc["metadata"] for doc in documents]
            self.collection.add(documents=docs_to_index, ids=ids, metadatas=metadata_to_index)