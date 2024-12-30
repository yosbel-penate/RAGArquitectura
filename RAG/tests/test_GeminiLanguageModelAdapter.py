import unittest
from RAG.src.language_model.GeminiLanguageModelAdapter import GeminiLanguageModelAdapter
from unittest.mock import patch, MagicMock
import os

class TestGeminiLanguageModelAdapter(unittest.TestCase):
    def setUp(self):
        # Configuración común para todos los tests
        self.mock_model = MagicMock()
        with patch('google.generativeai.GenerativeModel') as mock_gen_model: # Mockeamos GenerativeModel de la libreria
            mock_gen_model.return_value = self.mock_model
            self.adapter = GeminiLanguageModelAdapter()

    def test_init_api_key_from_env_success(self):
            with patch.dict(os.environ, {"GEMINI_API_KEY": "test_api_key"}):
                try:
                    GeminiLanguageModelAdapter()
                except Exception as e:
                    self.fail(f"Falló la inicialización del adaptador: {e}")

    def test_init_api_key_missing_error(self):
        with patch.dict(os.environ, clear=True):
            with self.assertRaises(ValueError) as context:
                GeminiLanguageModelAdapter()
            self.assertTrue("No se encontró la clave API de Gemini" in str(context.exception))

    def test_generate_text_success(self):
        """Test para generar texto con éxito."""
        self.mock_model.generate_content.return_value = MagicMock(text="Texto generado")
        prompt = "Escribe una historia"
        generated_text = self.adapter.generate_text(prompt)
        self.assertEqual(generated_text, "Texto generado")
        self.mock_model.generate_content.assert_called_once_with(prompt)

    def test_generate_text_no_text_error(self):
        """Test para cuando la respuesta de la API no contiene texto."""
        self.mock_model.generate_content.return_value = MagicMock(text=None)
        prompt = "Escribe un poema"
        generated_text = self.adapter.generate_text(prompt)
        self.assertEqual(generated_text, "Error: No se pudo generar texto.")
        self.mock_model.generate_content.assert_called_once_with(prompt)

    def test_generate_text_empty_prompt(self):
        """Test para un prompt vacío."""
        self.mock_model.generate_content.return_value = MagicMock(text="Respuesta para un prompt vacio")
        prompt = ""
        generated_text = self.adapter.generate_text(prompt)
        self.assertEqual(generated_text, "Respuesta para un prompt vacio")
        self.mock_model.generate_content.assert_called_once_with(prompt)
if __name__ == '__main__':
    unittest.main()