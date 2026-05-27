from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model=GoogleGenerativeAIEmbeddings("gemini-embedding-001")

Response=model.embed_query("What is the capital of France?")
print(Response)
