from agent_tool.time_tool import get_current_time
from agent_tool.wiki_search_tool import search_wikipedia
from agent_tool.calculator import calculate
from agent_tool.web_search_tool import web_search
from agent_tool.url_reader_tool import url_reader
from agent_tool.arvic_tool import arxiv_search
from langgraph.prebuilt import create_react_agent
from Core.llm import llm_model


tools = [get_current_time, search_wikipedia, calculate, web_search, url_reader, arxiv_search]
agent = create_react_agent(llm_model, tools)

async def get_response_stream(user_input: str):
    async for event in agent.astream_events(
        {"messages": [{"role": "user", "content": user_input}]},
        version="v1"
    ):
        if event["event"] == "on_chat_model_stream":
            content = event["data"]["chunk"].content
            if content:
                yield content
