import os

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

def main():
    directory = './documents'
    txt_files = get_txt_files(directory)
    all_chunks = []
    for file_path in txt_files:
        text = read_file(file_path)
        chunks = chunk_text(text)
        all_chunks.extend(chunks)
    # Aquí puedes hacer algo con all_chunks, como guardarlos en un archivo o procesarlos
    print(f"Total de fragmentos: {len(all_chunks)}")

if __name__ == "__main__":
    main()
