from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import json
import os

load_dotenv()

app = FastAPI()

# Store chat histories per session
chat_histories = {}

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

role_prompt = PromptTemplate(
    input_variables=["input", "role"],
    template="""You are a {role}.

Explain {input} for a beginner.

Return ONLY valid JSON:

{{
  "what": "...",
  "how": "...",
  "why": "..."
}}
"""
)


class QueryRequest(BaseModel):
    query: str
    role: str
    session_id: str


@app.post("/explain")
async def explain(request: QueryRequest):
    try:
        if request.session_id not in chat_histories:
            chat_histories[request.session_id] = []

        formatted_prompt = role_prompt.format(input=request.query, role=request.role)
        human_message = HumanMessage(content=formatted_prompt)
        chat_histories[request.session_id].append(human_message)

        response = llm.invoke(chat_histories[request.session_id])

        ai_message = AIMessage(content=response.content)
        chat_histories[request.session_id].append(ai_message)

        # Parse the JSON response
        try:
            parsed_response = json.loads(response.content)
        except json.JSONDecodeError:
            parsed_response = {
                "what": response.content,
                "how": "",
                "why": ""
            }

        return {"response": parsed_response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/", response_class=HTMLResponse)
async def get_frontend():
    with open("frontend/index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.get("/styles.css")
async def get_css():
    with open("frontend/styles.css", "r", encoding="utf-8") as f:
        from fastapi.responses import Response
        return Response(content=f.read(), media_type="text/css")


@app.get("/script.js")
async def get_js():
    with open("frontend/script.js", "r", encoding="utf-8") as f:
        from fastapi.responses import Response
        return Response(content=f.read(), media_type="application/javascript")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
