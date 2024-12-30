import unittest
from RAG.src.output.ConsoleOutputAdapter import ConsoleOutputAdapter

from unittest.mock import patch
import sys
import os

# Agregar la ruta al directorio src para importaciones relativas
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.insert(0, src_path)


class TestSimpleOutputAdapter(unittest.TestCase):
    def test_present_response(self):
        adapter = ConsoleOutputAdapter()
        response = "Esta es una respuesta de prueba."
        with patch('sys.stdout') as mock_stdout:
            adapter.present_response(response)
            mock_stdout.write.assert_any_call(response)
            mock_stdout.write.assert_any_call("\n")
            self.assertEqual(mock_stdout.write.call_count, 2)

if __name__ == '__main__':
    unittest.main()