from langchain_ollama import OllamaEmbeddings

model_name = "nomic-embed-text"
embedding = OllamaEmbeddings(model=model_name)

response = embedding.embed_query("Hello world")
print(response)