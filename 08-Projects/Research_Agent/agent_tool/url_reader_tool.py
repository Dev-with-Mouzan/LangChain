from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
@tool
def url_reader(url: str) -> str:
    """Read the content of a web page given its URL."""

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text()
    except Exception as e:
        return f"Error reading URL: {e}"