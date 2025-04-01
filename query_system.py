from transformers import pipeline
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def retrieve_relevant_chunks(query, chunk_embeddings, model):
    """
    Given a query, generate its embedding and find the top 3 most similar text chunks.
    
    Parameters:
        query (str): The input query.
        chunk_embeddings (dict): A dictionary where keys are text chunks and values are their embeddings.
        model (SentenceTransformer): The SentenceTransformer model used for encoding.
        
    Returns:
        list of tuples: Each tuple contains (text_chunk, similarity_score) for the top 3 similar chunks.
    """
    # Generate the embedding for the query
    query_embedding = model.encode(query)
    
    # Compute cosine similarity between the query and each chunk embedding
    similarities = {}
    for chunk, embedding in chunk_embeddings.items():
        sim = cosine_similarity([query_embedding], [embedding])[0][0]
        similarities[chunk] = sim
    
    # Sort the chunks by similarity in descending order and pick the top 3
    top_chunks = sorted(similarities.items(), key=lambda x: x[1], reverse=True)[:3]
    return top_chunks

def generate_response(retrieved_chunks, query):
    """
    Generates a text response using the "google/flan-t5-small" model based on the retrieved text chunks and a query.
    
    Parameters:
        retrieved_chunks (list): A list of tuples (text_chunk, similarity_score).
        query (str): The user query.
    
    Returns:
        str: The generated text response.
    """
    # Combine the retrieved chunks into a single context string
    combined_context = "\n\n".join([chunk for chunk, _ in retrieved_chunks])
    # Create a prompt by combining context and query
    prompt = f"Context:\n{combined_context}\n\nQuestion: {query}\nAnswer:"
    
    # Initialize the text generation pipeline using the Flan-T5 model
    generator = pipeline("text2text-generation", model="google/flan-t5-small")
    # Generate a response; you can adjust max_length as needed
    generated = generator(prompt, max_length=256)[0]['generated_text']
    return generated

if __name__ == "__main__":
    # Load the SentenceTransformer model used for generating embeddings
    sentence_transformer_model = SentenceTransformer("all-MiniLM-L6-v2")
    
    # Assume that chunk_embeddings has been generated already from your Selected_Document.txt
    # For example, from your embed_document.py file:
    #
    #     chunk_embeddings = embed_text_chunks(text_chunks)
    #
    # Ensure that the variable chunk_embeddings is available here.
    
    # For demonstration purposes, if you need to load or generate your embeddings:
    # from embed_document import split_document, embed_text_chunks
    # text_chunks = split_document("Selected_Document.txt")
    # chunk_embeddings = embed_text_chunks(text_chunks)
    
    # Get a query from the user
    query = input("Enter your query: ")
    
    # Retrieve the top 3 relevant text chunks
    top_chunks = retrieve_relevant_chunks(query, chunk_embeddings, sentence_transformer_model)
    
    # Generate and print the final response using the HuggingFace model
    response = generate_response(top_chunks, query)
    print("\nGenerated Response:")
    print(response)
