from json import load
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser

load_dotenv()
model = ChatOpenAI(model="openai/gpt-oss-20b", base_url="https://openrouter.ai/api/v1")

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","You are a professional sales Manager"),
        ("human","Create a Social Media Post to promote a new {product} launch")
    ]
)

chain = prompt_template | model | StrOutputParser()
result = chain.invoke({"product": "Smartphone X200 with advanced AI features"})

print("result: ", result)