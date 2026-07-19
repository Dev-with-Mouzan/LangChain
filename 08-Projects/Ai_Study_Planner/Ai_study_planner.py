# from langchain_google_genai import ChatGoogleGenerativeA
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv

load_dotenv()
llm = ChatOllama(model="llama3.2:latest ")



explain_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""You are a helpful assistant. Explain {topic} in detail."""
)

simply_prompt = PromptTemplate(
    input_variables=["text"],
    template="Simplify this for a beginner:\n{text} the answer is in key point like 1,2,3,4,5 and length of point is not more then 50 words"
)

fact_prompt = PromptTemplate(
    input_variables=["text"],
    template="provide a fact about {text} in detail. output is not more then 100 words"
)

question_prompt=PromptTemplate(
    input_variables=["text"],
    template="provide three question about {text} for a beginner. output is not more then 100 words"
)

parser=StrOutputParser()

explain=explain_prompt | llm | parser

simply=simply_prompt | llm | parser

fact_chain=fact_prompt | llm | parser

question_chain=question_prompt | llm | parser

def pipeline(input):
    topic=input["topic"]

    explaination=explain.invoke(topic)
    simple=simply.invoke(explaination)
    fact=fact_chain.invoke(topic)
    question=question_chain.invoke(topic)
    return {
        "explaination":explaination,
        "simple":simple,
        "fact":fact,
        "question":question
    }

run=RunnableLambda(pipeline)

response=run.invoke({"topic":"machine learning"})

print("Expanation:",response["explaination"])
print("Simple:",response["simple"])
print("Fact:",response["fact"])
print("Question:",response["question"])