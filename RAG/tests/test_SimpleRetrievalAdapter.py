import unittest
from unittest.mock import MagicMock
from RAG.src.retrieval.SimpleRetrievalAdapter import SimpleRetrievalAdapter
from RAG.src.core import IVectorStorePort

class TestSimpleRetrievalAdapter(unittest.TestCase):
    def setUp(self):
        """Configuración para cada test."""
        self.mock_vector_store = MagicMock()
        self.adapter = SimpleRetrievalAdapter(self.mock_vector_store)

    def test_retrieve_documents(self):
        """Test de recuperación de documentos."""
        query = "mi consulta"
        expected_result = ['doc1', 'doc2']
        self.mock_vector_store.search_fragments.return_value = expected_result
        result = self.adapter.retrieve_documents(query)
        self.assertEqual(result, expected_result)
        self.mock_vector_store.search_fragments.assert_called_once_with(query)

if __name__ == '__main__':
    unittest.main()
