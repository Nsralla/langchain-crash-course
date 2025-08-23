
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

load_dotenv()
model = ChatOpenAI(model="openai/gpt-oss-20b", base_url="https://openrouter.ai/api/v1")

# EXAMPLE 1 - PROMPT TEMPLATE WITH CHAT MODEL
text = "You are a helpful assistant. Generate a joke about {topic}"
prompt_template = PromptTemplate.from_template(text)
prompt = prompt_template.invoke({"topic": "cats"})
response = model.invoke(prompt)
print("response: ", response.content)

messages = [
    ("system", "You are a code debugger."),
    ("human", "given code below {code}, and error {error} help me fix, and debug")
]
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"code": "print('hello world'", "error": "SyntaxError: unexpected EOF while parsing"})
response = model.invoke(prompt)
print("response: ", response.content)