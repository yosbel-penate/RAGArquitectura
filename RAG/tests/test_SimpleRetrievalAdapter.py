import unittest
from unittest.mock import MagicMock
from RAG.src.retrieval.SimpleRetrievalAdapter import SimpleRetrievalAdapter
from RAG.src.core import IVectorStorePort

class TestSimpleRetrievalAdapter(unittest.TestCase):
    def setUp(self):
        # Crear un mock para VectorStorePort
        self.mock_vector_store_port = MagicMock(spec=IVectorStorePort)
        self.adapter = SimpleRetrievalAdapter(self.mock_vector_store_port)

    def test_retrieve_documents(self):
        # Configurar el mock para devolver un resultado específico
        query = "test query"
        expected_result = ["doc1", "doc2"]
        self.mock_vector_store_port().search_fragments.return_value = expected_result

        # Llamar al método y verificar el resultado
        result = self.adapter.retrieve_documents(query)
        self.assertEqual(result, expected_result)
        self.mock_vector_store_port().search_fragments.assert_called_once_with(query)

if __name__ == '__main__':
    unittest.main()
