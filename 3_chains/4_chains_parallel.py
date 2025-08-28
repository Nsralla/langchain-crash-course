from json import load
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableSequence, RunnableParallel
from typing import Any, Dict

from pyparsing import C

load_dotenv()
model = ChatOpenAI(model="openai/gpt-oss-20b", base_url="https://openrouter.ai/api/v1")

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","You are an expert product reviewer"),
        ("human","Please provide a review for the new {product}.")
    ]
)

def pros_template():
    pros_prompt = ChatPromptTemplate.from_messages(
        [
            ("system","You are an expert product reviewer"),
            ("human","Please list the pros of the new {product}.")
        ]
    )
    return pros_prompt


def cons_template():
    cons_prompt = ChatPromptTemplate.from_messages(
        [
            ("system","You are an expert product reviewer"),
            ("human","Please list the cons of the new {product}.")
        ]
    )
    return cons_prompt


pros_branch = pros_template() | model | StrOutputParser()
cons_branch = cons_template() | model | StrOutputParser()


chain = (
    prompt_template
    | model
    | StrOutputParser()
    | RunnableParallel(branches={"cons":cons_branch,"pros":pros_branch})
    | RunnableLambda(lambda x: f"Pros: {x['branches']['pros']}\nCons: {x['branches']['cons']}") #type: ignore
    )

result = chain.invoke({"product": "Iphone 13"})
print("result: ", result)