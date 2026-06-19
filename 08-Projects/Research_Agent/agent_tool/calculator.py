from langchain.tools import tool


@tool
def calculate(expression: str) -> str:
    """Perform a calculation and return the result."""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"