import gradio as gr
import time

from RAG.src.vector_store.ChromaVectorStoreAdapter import ChromaVectorStoreAdapter
from RAG.src.generation.SimpleGenerationAdapter import SimpleGenerationAdapter
from RAG.src.language_model.GeminiLanguageModelAdapter import GeminiLanguageModelAdapter
from RAG.src.generation.template_formating_promp import load_template_formating_promp
from tools import load_docs_from_json_file
import os

persist_directory = os.path.join(os.path.dirname(__file__), 'vectorDB')
if not os.path.exists(persist_directory):
    os.makedirs(persist_directory)

documentos = load_docs_from_json_file()
vector_store_adapter = ChromaVectorStoreAdapter(persist_directory=persist_directory)
vector_store_adapter.index_documents(documentos)
generation_adapter = SimpleGenerationAdapter(GeminiLanguageModelAdapter(), load_template_formating_promp)

with gr.Blocks(fill_height=True) as demo:
    gr.Markdown("# Soy Alex, tu asistente IA de programación. 🤗")
    chatbot = gr.Chatbot(scale=1)
    msg = gr.Textbox(scale=0, label="Pregunta")
    clear = gr.Button("Limpiar")

    def user(user_message, history):
        return "", history + [[user_message, None]]

    def bot(history):
        query=history[-1][0]
        results = vector_store_adapter.search_fragments(query)
        bot_message = generation_adapter.generate_response(results, query)
        time.sleep(2)
        history[-1][1] = bot_message
        return history

    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, chatbot, chatbot
    )
    clear.click(lambda: None, None, chatbot, queue=False)

demo.launch()
