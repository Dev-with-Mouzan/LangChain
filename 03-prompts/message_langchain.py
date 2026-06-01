"""There are three type of Messages in Langchain
1. HumanMessage
2. AIMessage
3. SystemMessage
Each message type is used to represent different participants in a conversation with a language model.

"""
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

messages = [
    SystemMessage(content="You are a Rude Teacher")
    #
]
while True:
    user_input = input("Write your Query here: ")
    messages.append(HumanMessage(content=user_input))
    
   
    response = llm.invoke(messages)
    
    print("Ai:", response.content)
    
    messages.append(AIMessage(content=response.content))