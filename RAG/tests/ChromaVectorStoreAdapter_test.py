import unittest
from unittest.mock import MagicMock
from src.vector_store.ChromaVectorStoreAdapter import ChromaVectorStoreAdapter

class ChromaVectorStoreAdapter(unittest.TestCase):

    def setUp(self):
        self.adapter = ChromaVectorStoreAdapter()
        self.adapter.client = MagicMock()

    def test_search_fragments(self):
        query = "test query"
        expected_results = [{'fragment': 'fragment1'}, {'fragment': 'fragment2'}]
        self.adapter.client.query.return_value = expected_results

        results = self.adapter.search_fragments(query)
        self.assertEqual(results, ['fragment1', 'fragment2'])
        self.adapter.client.query.assert_called_once_with(query)

    def test_index_documents(self):
        documents = ['doc1', 'doc2']
        self.adapter.index_documents(documents)
        self.assertEqual(self.adapter.client.index.call_count, len(documents))
        self.adapter.client.index.assert_any_call('doc1')
        self.adapter.client.index.assert_any_call('doc2')

if __name__ == '__main__':
    unittest.main()
