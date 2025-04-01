Step 1: Select and Load a Document

Choose a Document:

Jack White on the Most Stubborn and Prophetic Music of His Career
https://www.vulture.com/2022/07/interview-jack-white-best-worst-superlatives.html

Select a document of interest (e.g., a web page, text file, or downloaded article).
The document can be in any accessible format that allows text extraction (e.g., plain text, HTML).

Prompt an AI Tool for Assistance:
Use the following prompt with an AI tool (such as ChatGPT) to generate code for loading and preparing the document:

Prompt used: 

“Write Python code to read this article of an interview with the artist Jack White, which is content from a web page, Vulture. As the document is a web page, use BeautifulSoup to extract the relevant text. Provide the text as a cleaned string for further processing.”

Verify the Output:


Ensure the loaded and cleaned content is saved in a file named Selected_Document.txt.
Save the Selected_Document.txt file in your GitHub repository.

-Done-


Step 2: Install Required Libraries


Install Libraries:


Use the following prompt to generate installation commands:


“Write the terminal commands needed to install the following Python libraries: sentence-transformers, transformers, pandas, and scikit-learn.”

Responses:

pip install sentence-transformers transformers pandas scikit-learn
sentence-transformers
transformers
pandas
Scikit-learn
pip install -r requirements.txt



Include a requirements.txt File:
Generate and include a requirements.txt file to allow users to easily install the dependencies.
-Done-


Step 3: Generate Embeddings and Store Locally


Load the Selected Document:
Use the following prompt to generate code that reads the text from Selected_Document.txt and splits it into manageable chunks:

“Write Python code that reads the content of a file called "Selected_Document.txt" and splits it into chunks separated by double newline characters ("\n\n").” -done-

Generate Embeddings:
Use this prompt to generate code for embedding the document content:


“Write Python code that uses the SentenceTransformers library and the model "all-MiniLM-L6-v2" to generate embeddings for a list of text chunks. Store the embeddings in a Python dictionary along with their associated text.” -done-


Store Embeddings in Memory:
Ensure the embeddings and their associated text are stored in a dictionary for retrieval.
Save the embedding code in your GitHub repository. -done-


Step 4: Query the System

Retrieve Relevant Content Using Cosine Similarity:
Use this prompt to generate retrieval code:

“Write Python code that takes a query as input, generates its embedding using SentenceTransformers, and finds the top 3 most similar text chunks from a dictionary of embeddings using cosine similarity from scikit-learn.”

Generate a Response Using a HuggingFace Model:
Use this prompt to generate response code:

“Write Python code that uses the HuggingFace Transformers library and the "google/flan-t5-small" model to generate a text response based on retrieved text chunks and a query. Combine the chunks into a single prompt before generating the response. The program should take user queries as input rather than hardcoding them.” -done-

Save the Query System Code:
Save all code for querying and generating responses in your GitHub repository. -done-

Test with Example Queries:
Interact with your program by entering at least three example queries. Save these queries and the program’s output (including retrieved content and generated responses).

What is Jack Whites thoughts on live performances?

	Answer:
"Jack White believes that live performances are a dynamic mix of spontaneity and precision, where the unpredictability of the moment creates a unique and engaging connection with the audience."

How does Jack White describe his own creative process?

Answer:
	"According to Jack White, his creative process is very experimental and fluid. He lets ideas evolve naturally without following a strict formula, creating a dialogue between inspiration and experience."

What does Jack say about his worst performance?

Answer:
"Jack White describes his worst performance as a challenging yet invaluable learning experience. He believes that even the most problematic shows offer insights that can lead to better performances in the future."




Step 5: Deepen Your Understanding of the Program

Ask the AI for Questions to Understand the Program:
Use the following prompt to generate a list of questions to better understand the program and its components:

What are five important questions I should ask to understand how this program works? Please include questions about concepts such as cosine similarity, sentence-transformers, and the role of embeddings.

Include these questions and their AI-generated answers in your reflection report.

What are embeddings and what role do they play in this program?
Answer: Embeddings are dense numerical representations of text that capture the semantic meaning of words, phrases, or entire documents. In our program, embeddings convert both the document’s text chunks and the user query into fixed-length vectors. This conversion enables us to measure the similarity between texts using vector operations, making it possible to retrieve the most relevant chunks from the document when a query is made.

How does the SentenceTransformers library work, and why is the "all-MiniLM-L6-v2" model used in this project?
Answer: The SentenceTransformers library is designed to generate high-quality text embeddings using pre-trained transformer models. The "all-MiniLM-L6-v2" model, in particular, offers a good balance between performance and computational efficiency. It generates embeddings that effectively capture the semantics of text, making it ideal for comparing the similarity of text chunks and queries in our retrieval system.

What is cosine similarity and how is it used to retrieve relevant text chunks?
Answer: Cosine similarity is a metric that measures the cosine of the angle between two vectors. In our program, it is used to quantify how similar the embedding of a user's query is to the embeddings of text chunks from the document. By computing this similarity, the system can rank the chunks and retrieve the top three that best match the query, ensuring that the most contextually relevant pieces of text are used in generating a response.

How does the program integrate the retrieved text chunks with the user query to generate a final response using a HuggingFace model?
Answer: Once the top relevant text chunks are retrieved using cosine similarity, the program combines these chunks into a single context string. This context, along with the original user query, is used to form a comprehensive prompt. The HuggingFace model ("google/flan-t5-small") then processes this prompt to generate a coherent and contextually informed response, ensuring that the answer is both accurate and relevant to the query.

What are the advantages of using a Retrieval-Augmented Generation (RAG) system compared to a standard text generation model?
Answer: A RAG system enhances response quality by grounding the generated answers in specific, relevant information from a source document. Unlike standard text generation models that rely solely on learned patterns, a RAG system retrieves pertinent content from the document via embeddings and cosine similarity. This ensures that the generated response is not only contextually relevant but also backed by the actual content of the document, leading to more accurate and trustworthy outputs


Reflection Report:
The reflection should include:

The name and an explanation of the document being queried.

Jack White on the Most Stubborn and Prophetic Music of His Career
https://www.vulture.com/2022/07/interview-jack-white-best-worst-superlatives.html


A basic explanation of how the program works, based on a query to the AI (e.g., "What is cosine similarity?").

1) Document Processing: read the document
2) Generating Embeddings: text chunks converted into a numerical vector
3) Query Handling: system generates an embedding for this query using the same model
4) Retrieving Relevant Chunks: calculates the cosine similarity between the query embedding and each text chunk’s embedding, the top three text chunks with the highest similarity scores are selected as the most relevant
5) Generating a Response: retrieved text chunks are combined into a single context. This context, along with the query, is fed into a HuggingFace model. The model processes this prompt to generate a coherent response that uses both the retrieved context and the query.


Five important questions about how the model works and their AI-generated answers.
-Done above-

An analysis of:

-How well the system retrieved relevant content.

The system usually found the right parts of the article that match the question. When you ask something clear and specific, it tends to grab the best pieces of text.

Sometimes, if the question is too vague or just worded differently, the system might not pick the most useful parts out of the article. The way you ask the question can change what content it pulls out.

-The quality of the generated responses.

The responses I get are normally easy to understand and make sense, because they mix the important parts of the article with the question.
Every now and then the answers feel a bit generic and miss some of the details from the article. This is something that could be improved.

-Possible improvements or extensions to the system.

1) The system could be improved by helping the user rephrase the question
2) Experimenting with different ways to break the article into chunks could help with accuracy
3) Training the response generator a bit more on similar content/articles may help it produce answers that are more thorough
4) Adding a feature where the user could say if a response was helpful or not

Include the program output (queries, retrieved content, and generated responses) within the report. -done above-
