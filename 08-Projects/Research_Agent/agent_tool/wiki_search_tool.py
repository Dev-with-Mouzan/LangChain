from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import tool

@tool
def search_wikipedia(query: str) -> str:
    """Search Wikipedia and return a summary of the article."""
    api_wrapper = WikipediaAPIWrapper(top_k_results=3, doc_content_chars_max=500)
    wiki = WikipediaQueryRun(api_wrapper=api_wrapper)
    return wiki.run(query)



