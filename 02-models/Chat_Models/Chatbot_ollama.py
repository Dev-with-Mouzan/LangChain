from langchain_ollama import ChatOllama 

llm = ChatOllama(model="llama3.2:3b")# we can use any model that we have locally

response = llm.invoke(x:=input("Write your Query here: "))
print("Ai:",response.content)