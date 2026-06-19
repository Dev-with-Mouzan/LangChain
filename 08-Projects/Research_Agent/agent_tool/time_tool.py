from datetime import datetime
from langchain.tools import tool

@tool
def get_current_time(dummy: str="") -> str:
    """Return the current time."""
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

