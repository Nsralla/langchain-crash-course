from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()
model = ChatOpenAI(model="openai/gpt-oss-20b", base_url="https://openrouter.ai/api/v1")

messages = [
    SystemMessage(content="You are a helpful assistant, specializing in providing information about various topics."),
    HumanMessage(content="Who created Google?")
]

response = model.invoke(messages)
print("FULL RESPONSE: ", response)
print("ANSWER: ", response.content)

messages = [
    SystemMessage(content="You are a helpful assistant, specializing in providing information about various topics."),
    HumanMessage(content="Who created Google?"),
    AIMessage(content="Google was created by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University."),
    HumanMessage(content="When was it founded?")
]
response = model.invoke(messages)
print("FULL RESPONSE: ", response)
print("ASNWER: ", response.content)