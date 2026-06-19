from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
load_dotenv()

llm_model = ChatOpenAI(
    model="qwen/qwen3-8b",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    temperature=0,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)


