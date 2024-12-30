import unittest
from unittest.mock import MagicMock
from RAG.src.generation.SimpleGenerationAdapter import SimpleGenerationAdapter
from RAG.src.core.ILanguageModelPort import ILanguageModelPort

class TestSimpleGenerationAdapter(unittest.TestCase):
    def setUp(self):
        self.mock_language_model = MagicMock(spec=ILanguageModelPort)
        self.adapter = SimpleGenerationAdapter(self.mock_language_model)

    def test_generate_response(self):
        documents = ["Documento 1", "Documento 2"]
        query = "¿Cuál es el contenido del documento 1?"
        expected_prompt = f"Query: {query}\nDocuments: {documents}"
        self.mock_language_model.generate_text.return_value = "Respuesta generada"

        response = self.adapter.generate_response(documents, query)

        self.mock_language_model.generate_text.assert_called_once_with(expected_prompt)
        self.assertEqual(response, "Respuesta generada")

if __name__ == '__main__':
    unittest.main()
