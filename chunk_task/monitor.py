import os
import json

def get_txt_files(directory):
    txt_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                txt_files.append(os.path.join(root, file))
    return txt_files

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def chunk_text(text, chunk_size=5000, overlap=1000):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def save_chunks_to_file(chunks, output_file, file_name):
    chunks_json = {"docs": [{"doc": chunk, "metadata": {"file_name": file_name}} for chunk in chunks]}
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(chunks_json, file, ensure_ascii=False, indent=4)

def main():
    current_dir = os.path.dirname(__file__)
    directory = os.path.join(current_dir, 'documents')
    txt_files = get_txt_files(directory)
    all_chunks = []
    for file_path in txt_files:
        text = read_file(file_path)
        chunks = chunk_text(text)
        all_chunks.extend([{"doc": chunk, "metadata": {"file_name": os.path.basename(file_path)}} for chunk in chunks])
    save_chunks_to_file(all_chunks, os.path.join(current_dir, 'chunk.json'), os.path.basename(file_path))
    print(f"Total de fragmentos: {len(all_chunks)}")

if __name__ == "__main__":
    main()
