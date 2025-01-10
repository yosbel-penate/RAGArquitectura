import json


def load_docs_from_json_file():
    with open('chunk_task/chunk.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        documentos = [doc['doc'] for doc in data['docs']]
    return documentos