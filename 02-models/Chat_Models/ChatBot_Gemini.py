from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chat = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

response = chat.invoke(x:=input("Write your Query here: "))
print("Ai:",response.content)
