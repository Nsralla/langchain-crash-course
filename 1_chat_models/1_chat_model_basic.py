from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
model = ChatOpenAI(model="openai/gpt-oss-20b", base_url="https://openrouter.ai/api/v1")

response = model.invoke("Who created google?")
print("FULL RESPONSE:", response)
print("Result: ",response.content)