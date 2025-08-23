from json import load
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
import os


load_dotenv()
PROJECT_ID = os.getenv("FIREBASE_PROJECT_ID")
SESSION_ID = "user_session_new"
COLLECTION_NAME = "chat_history"
model = ChatOpenAI(model="openai/gpt-oss-20b", base_url="https://openrouter.ai/api/v1")



print("Initializing Firestore...")
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=firestore.Client(project=PROJECT_ID)
)

print("chat history initialized.")
print("CHAT HISTORY: ", chat_history)

while True:
    user_query = input("user: ")
    if user_query.lower() in ["exit", "quit"]:
        break
    chat_history.add_user_message(user_query)
    response = model.invoke(chat_history.messages)
    chat_history.add_ai_message(response.content)
    print(response.content)

