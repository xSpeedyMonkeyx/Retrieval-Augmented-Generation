# embed_document.py

from sentence_transformers import SentenceTransformer

def split_document(file_path):
    """
    Reads the content of the specified file and splits it into chunks
    separated by double newline characters.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().strip()
    chunks = [chunk.strip() for chunk in content.split("\n\n") if chunk.strip()]
    return chunks

def embed_text_chunks(chunks):
    """
    Generates embeddings for a list of text chunks using the
    'all-MiniLM-L6-v2' model.
    """
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(chunks, show_progress_bar=True)
    chunk_embeddings = {chunk: embedding for chunk, embedding in zip(chunks, embeddings)}
    return chunk_embeddings

if __name__ == "__main__":
    # 1. Split the document
    file_path = "Selected_Document.txt"
    text_chunks = split_document(file_path)
    
    # 2. Embed the chunks
    embeddings_dict = embed_text_chunks(text_chunks)
    
    print(f"Generated embeddings for {len(embeddings_dict)} chunks.")
    # Optionally, print each chunk and its embedding
    for chunk, embedding in embeddings_dict.items():
        print("\nChunk:", chunk)
        print("Embedding:", embedding)
