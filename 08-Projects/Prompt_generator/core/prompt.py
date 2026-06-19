from langchain_core.prompts import PromptTemplate
from core.llm import llm_model
from langchain_core.output_parsers import StrOutputParser

template = PromptTemplate(
    input_variables=["topic","tone"],
    template="""
You are a Senior AI Prompt Engineer.

Convert the following user requirement into a professional prompt.

User Requirement:
{topic}

Tone:
{tone}

Structure the generated prompt into:

ROLE:
Who the AI should act as.

GOAL:
What the AI should accomplish.

CONTEXT:
Important background information.

INSTRUCTIONS:
Step-by-step guidance.

CONSTRAINTS:
Rules the AI must follow.

OUTPUT FORMAT:
Expected response format.

Generate only the final prompt.
""")

parser=StrOutputParser()

chain=template | llm_model | parser


def generate_prompt(user_input, tone):
    response = chain.invoke({"topic": user_input, "tone": tone})
    return response