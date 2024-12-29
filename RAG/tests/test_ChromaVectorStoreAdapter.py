import unittest
from unittest.mock import MagicMock
import sys
import os

# Agregar la ruta al directorio src para importaciones relativas
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.insert(0, src_path)

from vector_store.ChromaVectorStoreAdapter import ChromaVectorStoreAdapter

class TestChromaVectorStoreAdapter(unittest.TestCase):

    def setUp(self):
        """Configuración para cada test."""
        self.mock_client = MagicMock()
        self.adapter = ChromaVectorStoreAdapter()
        self.adapter.client = self.mock_client  # Inyectar el mock

    def test_search_fragments_success(self):
        """Test de búsqueda de fragmentos exitosa."""
        mock_results = {
            'results': [{
                'documents': ["fragment1", "fragment2"]
            }]
        }
        self.mock_client.query.return_value = mock_results
        query = "mi consulta"
        results = self.adapter.search_fragments(query)
        self.assertEqual(results, [["fragment1", "fragment2"]])
        self.mock_client.query.assert_called_once_with(query_texts=[query])

    def test_search_fragments_empty(self):
        """Test de búsqueda de fragmentos vacía."""
        mock_results = {
            'results': [{
                'documents': []
            }]
        }
        self.mock_client.query.return_value = mock_results
        query = "mi consulta"
        results = self.adapter.search_fragments(query)
        self.assertEqual(results, [[]])
        self.mock_client.query.assert_called_once_with(query_texts=[query])

    def test_index_documents_success(self):
        """Test de indexado de documentos exitoso."""
        documents = ["documento1", "documento2"]
        self.adapter.index_documents(documents)
        self.mock_client.add.assert_called_once_with(documents=documents)

    def test_index_documents_empty(self):
        """Test de indexado de documentos con una lista vacía."""
        documents = []
        self.adapter.index_documents(documents)
        self.mock_client.add.assert_called_once_with(documents=[])

    def test_index_documents_single(self):
        """Test de indexado de documentos con un solo documento"""
        documents = ["documento1"]
        self.adapter.index_documents(documents)
        self.mock_client.add.assert_called_once_with(documents=documents)

if __name__ == '__main__':
    unittest.main()