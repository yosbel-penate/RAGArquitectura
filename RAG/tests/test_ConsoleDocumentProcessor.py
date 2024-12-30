import unittest
from unittest.mock import MagicMock
from RAG.src.user.ConsoleDocumentProcessor import ConsoleDocumentProcessor
from RAG.src.vector_store.ChromaVectorStoreAdapter import ChromaVectorStoreAdapter

class TestConsoleDocumentProcessor(unittest.TestCase):
    def setUp(self):
        self.vector_store_adapter = ChromaVectorStoreAdapter()
        self.vector_store_adapter.index_documents = MagicMock()
        self.processor = ConsoleDocumentProcessor(self.vector_store_adapter, ["Documento 1", "Documento 2"])

    def test_process_documents(self):
        self.processor.process_documents_and_get_answer()
        self.vector_store_adapter.index_documents.assert_called_once_with(["Documento 1", "Documento 2"])

if __name__ == '__main__':
    unittest.main()
