from json import load
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableSequence
from typing import Any, Dict

load_dotenv()
model = ChatOpenAI(model="openai/gpt-oss-20b", base_url="https://openrouter.ai/api/v1")

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","You are a professional sales Manager"),
        ("human","Create a Social Media Post to promote a new {product} launch")
    ]
)

upper_case_output = RunnableLambda(lambda x: x.upper())
custom_output = RunnableLambda(lambda x: f"Word count: {len(x.split())}\n{x}")

chain = prompt_template | model | StrOutputParser() | upper_case_output | custom_output
result = chain.invoke({"product": "Smartphone X200 with advanced AI features"})
print("result: ", result)