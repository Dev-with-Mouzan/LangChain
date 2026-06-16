from langchain_ollama import ChatOllama
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

llm=ChatOllama(model="llama3.2:1b")

search_tool=DuckDuckGoSearchRun()

prompt=hub.pull("hwehase17/react")

agent=create_react_agent(llm,tools=[search_tool],prompt=prompt)

llm_Agent=AgentExecutor(agent=agent,tools=[search_tool],verbose=True)

response=llm_Agent.invoke("What is LangChain?")

print(response)