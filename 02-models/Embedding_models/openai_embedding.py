from langchain_openai_embedding import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model=OpenAIEmbeddings(model="text-embedding-3-small")

response = model.embed_query("What is LangChain?")
print("Embedding:", response)

