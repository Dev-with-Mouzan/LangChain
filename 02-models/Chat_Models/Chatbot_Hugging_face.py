from langchain_huggingface import ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

model=ChatHuggingFace(model="microsoft/DialoGPT-medium") # we can use any model that is available on hugging face
responde = model.invoke(x:=input("Write your Query here: "))
print("Ai:",responde.content)
