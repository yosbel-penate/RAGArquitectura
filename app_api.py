from flask import Flask, request, jsonify
from RAG.src.vector_store.ChromaVectorStoreAdapter import ChromaVectorStoreAdapter
from RAG.src.generation.SimpleGenerationAdapter import SimpleGenerationAdapter
from RAG.src.language_model.GeminiLanguageModelAdapter import GeminiLanguageModelAdapter


app = Flask(__name__)

vector_store_adapter = ChromaVectorStoreAdapter()
generation_adapter = SimpleGenerationAdapter(GeminiLanguageModelAdapter())

documentos = [
        "París es la capital de Francia.",
        "Berlín es la capital de Alemania.",
        "Madrid es la capital de España."
    ]
vector_store_adapter.index_documents(documentos)

@app.route('/add_documents', methods=['POST'])
def add_documents():
    documentos = request.json.get('documents', [])
    vector_store_adapter.index_documents(documentos)
    return jsonify({"status": "success"}), 200

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    results = vector_store_adapter.search_fragments(query)
    return jsonify({"results": results}), 200

@app.route('/generate_answer', methods=['POST'])
def generate_answer():
    query = request.json.get('query')
    results = vector_store_adapter.search_fragments(query)
    answer = generation_adapter.generate_response(query, results)
    return jsonify({"answer": answer}), 200

@app.route('/get_document/<doc_id>', methods=['GET'])
def get_document(doc_id):
    document = vector_store_adapter.get_document(doc_id)
    return jsonify({"document": document}), 200

@app.route('/delete_document/<doc_id>', methods=['DELETE'])
def delete_document(doc_id):
    vector_store_adapter.delete_document(doc_id)
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True)