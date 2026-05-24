from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(model="gpt-4o", temperature=0.9)

response = chat.invoke(x:=input("Write your Query here: "))
print("Ai:",response.content)
