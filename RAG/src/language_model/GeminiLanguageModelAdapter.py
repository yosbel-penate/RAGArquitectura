from RAG.src.core.ports import LanguageModelPort
import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()

class GeminiLanguageModelAdapter(LanguageModelPort):
    def __init__(self):
        # Obtener la clave API de las variables de entorno
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("No se encontró la clave API de Gemini en las variables de entorno. Por favor, configura 'GEMINI_API_KEY' en tu archivo .env o en tus variables de entorno.")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')


    def generate_text(self, prompt: str) -> str:
        # Implementación de la generación de texto usando google-generativeai
        response = self.model.generate_content(prompt)
        if response.text:
            return response.text
        else:
            return "Error: No se pudo generar texto."