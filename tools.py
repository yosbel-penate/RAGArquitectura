import json

from bs4 import BeautifulSoup



def load_docs_from_json_file():
    with open('chunk_task/chunk.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        documentos = [{'doc': doc['doc'], 'metadata': doc['metadata']} for doc in data]
    return documentos


def clean_unsupported_telegram_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    for tag in soup.find_all(True):
        if tag.name not in ["b", "strong", "i", "em", "u", "ins", "s", "strike", "del", "code", "pre", "a"]:
            tag.unwrap()
    return str(soup).strip()


def format_for_telegram(text):
    """
    Formatea el texto HTML para que sea visualizado correctamente en Telegram.
    """
    text = text.replace("```html", "")
    text = text.replace("```", "")

    return clean_unsupported_telegram_tags(text)