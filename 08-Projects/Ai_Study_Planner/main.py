from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="AI Study Planner")

app.mount("/static", StaticFiles(directory="static"), name="static")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
parser = StrOutputParser()

explain_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""You are a helpful assistant. Explain {topic} in detail.

Use markdown formatting with:
- **Bold** for key terms and important concepts
- ## Headers for main sections
- ### Subheaders for subsections
- Bullet points (- ) for lists
- > Blockquotes for important notes

Keep the explanation clear and well-structured. Aim for 200-300 words."""
)

simplify_prompt = PromptTemplate(
    input_variables=["text"],
    template="""Simplify this for a beginner:

{text}

Create a simplified version with:
- Use numbered lists (1. 2. 3.) for key points
- Keep each point under 50 words
- Use **bold** for important terms
- Make it easy to understand

Provide 4-5 key points."""
)

fact_prompt = PromptTemplate(
    input_variables=["text"],
    template="""Provide an interesting fact about {text}.

Use markdown formatting:
- **Bold** for the main fact
- Add context or background information
- Keep it under 100 words
- Make it engaging and memorable"""
)

question_prompt = PromptTemplate(
    input_variables=["text"],
    template="""Provide three practice questions about {text} for a beginner.

Format as:
**Question 1:** [question]
**Answer:** [brief answer]

**Question 2:** [question]
**Answer:** [brief answer]

**Question 3:** [question]
**Answer:** [brief answer]

Keep each answer under 50 words."""
)

explain_chain = explain_prompt | llm | parser
simplify_chain = simplify_prompt | llm | parser
fact_chain = fact_prompt | llm | parser
question_chain = question_prompt | llm | parser


class TopicRequest(BaseModel):
    topic: str


@app.get("/")
async def root():
    return FileResponse("static/index.html")


@app.post("/api/study-plan")
async def study_plan(request: TopicRequest):
    try:
        topic = request.topic.strip()
        if not topic:
            raise HTTPException(status_code=400, detail="Topic cannot be empty")

        explanation = explain_chain.invoke(topic)
        simplified = simplify_chain.invoke(explanation)
        fact = fact_chain.invoke(topic)
        questions = question_chain.invoke(topic)

        return {
            "explanation": explanation,
            "simplified": simplified,
            "fact": fact,
            "questions": questions
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
