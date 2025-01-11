import unittest
from unittest.mock import Mock
from RAG.src.generation.SimpleGenerationAdapter import SimpleGenerationAdapter
from RAG.src.core.ILanguageModelPort import ILanguageModelPort
from RAG.src.generation.template_formating_promp import load_template_formating_promp

class TestSimpleGenerationAdapter(unittest.TestCase):
    def setUp(self):
        self.mock_language_model = Mock()
        self.mock_template_formatter = Mock()
        self.adapter = SimpleGenerationAdapter(self.mock_language_model, self.mock_template_formatter)

    def test_generate_response(self):
        documents = [
            {'metadata': {'file_name': 'doc1.txt'}},
            {'metadata': {'file_name': 'doc2.txt'}},
            {'metadata': {'file_name': 'doc1.txt'}}
        ]
        query = "What is the capital of France?"
        self.mock_template_formatter.return_value = "formatted prompt"
        self.mock_language_model.generate_text.return_value = "Paris is the capital of France."

        response = self.adapter.generate_response(documents, query)

        self.mock_template_formatter.assert_called_once()
        self.mock_language_model.generate_text.assert_called_once_with("formatted prompt")
        self.assertIn("Paris is the capital of France.", response)
        self.assertIn("\n\nReferences:\n1. doc1\n2. doc2\n", response)

    def test_extract_unique_file_names(self):
        documents=[{'document': [...], 'metadata': [{'file_name': 'doc1.txt'}, {'file_name': 'doc2.txt'}, {'file_name': 'doc1.txt'}]}]
        expected_file_names = ['doc1', 'doc2']
        file_names = self.adapter.extract_unique_file_names(documents)
        self.assertEqual(sorted(file_names), sorted(expected_file_names))

    def test_create_enumerated_references(self):
        file_names = ['doc1', 'doc2']
        expected_references = "\n\nReferences:\n1. doc1\n2. doc2\n"
        references = self.adapter.create_enumerated_references(file_names)
        self.assertEqual(references, expected_references)

if __name__ == '__main__':
    unittest.main()
