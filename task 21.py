import os
from openai import OpenAI

# 1. The Retriever (Mocked for this example)
def retrieve_chunks(query, top_k=3):
    """
    In a real application, this connects to your Vector DB (e.g., Chroma, FAISS).
    For now, we mock it with a simple keyword search over a dummy database.
    """
    mock_database = [
        "The Linux kernel, created by Linus Torvalds, is the core of Ubuntu and other distributions.",
        "Ubuntu uses the APT package manager to handle software installations.",
        "RAG stands for Retrieval-Augmented Generation, combining search with LLMs.",
        "The quick brown fox jumps over the lazy dog."
    ]
    
    # Simple mock retrieval: returns chunks containing words from the query
    relevant_chunks = [
        doc for doc in mock_database 
        if any(word.lower() in doc.lower() for word in query.split())
    ]
    return relevant_chunks[:top_k]

# 2. Prompt Builder
def build_prompt(query, retrieved_chunks):
    """
    Stitches the chunks together and enforces strict grounding rules.
    """
    # Connect chunks with a clear visual separator
    context_string = "\n---\n".join(retrieved_chunks)

    # The foundational RAG Prompt Template
    prompt = f"""You are a precise, document-based Q&A assistant.
Use the following pieces of retrieved context to answer the question.
If you don't know the answer based on the context, just say "I do not have enough information to answer that." 
Do not make up information.

Context:
{context_string}

Question: {query}
Answer:"""
    return prompt

# 3. LLM Generator
def generate_answer(prompt):
    """
    Sends the constructed prompt to the LLM.
    """
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.0 # Low temperature for factual consistency
    )
    return response.choices[0].message.content

# 4. CLI Application Loop
def main():
    print("Welcome to the Document Q&A CLI! (Type 'exit' to quit)")
    print("-" * 50)
    
    while True:
        try:
            query = input("\n📝 Enter your question: ")
            if query.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break
            
            if not query.strip():
                continue

            print("🔍 Retrieving relevant chunks...")
            chunks = retrieve_chunks(query)

            if not chunks:
                print("⚠️ No relevant information found in the documents.")
                continue

            print("🤖 Generating answer...")
            prompt = build_prompt(query, chunks)
            answer = generate_answer(prompt)

            print(f"\n💬 Answer:\n{answer}")
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")

if __name__ == "__main__":
    main()