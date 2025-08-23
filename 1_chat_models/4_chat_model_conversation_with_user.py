
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from sympy import true

load_dotenv()
model = ChatOpenAI(model="openai/gpt-oss-20b", base_url="https://openrouter.ai/api/v1")
chat_history = []
system_message = SystemMessage(content="You are a helpful assistant, specializing in providing information about various topics.")
chat_history.append(system_message)

while true:
    user_input = input("User: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    user_message = HumanMessage(content=user_input)
    chat_history.append(user_message)
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(response.content))
    print("AI response: ", response.content)