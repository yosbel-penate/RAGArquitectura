import unittest
from unittest.mock import MagicMock
from RAG.src.vector_store.ChromaVectorStoreAdapter import ChromaVectorStoreAdapter

class TestChromaVectorStoreAdapter(unittest.TestCase):
    def setUp(self):
        self.adapter = ChromaVectorStoreAdapter()
        self.adapter.client = MagicMock()
        self.adapter.collection = MagicMock()

    def test_search_fragments(self):
        query = "test query"
        expected_result = ["document1", "document2"]
        self.adapter.collection.query.return_value = {"documents": expected_result}

        result = self.adapter.search_fragments(query)
        self.assertEqual(result, expected_result)
        self.adapter.collection.query.assert_called_once_with(query_texts=[query])

    def test_index_documents(self):
        documents = ["doc1", "doc2"]
        self.adapter.index_documents(documents)
        ids = [str(i) for i in range(len(documents))]
        self.adapter.collection.add.assert_called_once_with(documents=documents, ids=ids)

    def test_index_documents_empty(self):
        with self.assertRaises(ValueError):
            self.adapter.index_documents([])

if __name__ == '__main__':
    unittest.main()
