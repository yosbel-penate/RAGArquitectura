import unittest
from app_api import app

class AppApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_documents(self):
        response = self.app.post('/add_documents', json={'documents': ['doc1', 'doc2']})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "success"})

    def test_search(self):
        response = self.app.get('/search', query_string={'query': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('results', response.json)

    def test_generate_answer(self):
        response = self.app.post('/generate_answer', json={'query': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('answer', response.json)

    def test_get_document(self):
        response = self.app.get('/get_document/doc1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('document', response.json)

    def test_delete_document(self):
        response = self.app.delete('/delete_document/doc1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "success"})

if __name__ == '__main__':
    unittest.main()
