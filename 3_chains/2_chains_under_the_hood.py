from json import load
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableSequence
from typing import Any, Dict

load_dotenv()
model = ChatOpenAI(model="openai/gpt-oss-20b", base_url="https://openrouter.ai/api/v1")

prompt= ChatPromptTemplate.from_messages(
    [
        ("system","You are a professional sales Manager"),
        ("human","Create a Social Media Post to promote a new {product} launch")
    ]
)

# Add type hints to inform Pylance about the expected types
format_prompt = RunnableLambda(lambda x: prompt.format_prompt(**x)) 
invoke_model = RunnableLambda(lambda x: model.invoke(x.to_messages()))  # type: ignore
parsed_output = RunnableLambda(lambda x: x.content)  # type: ignore

chain = RunnableSequence(format_prompt, invoke_model, parsed_output)
result = chain.invoke({"product": "Smartphone X200 with advanced AI features"})
print("result: ", result)