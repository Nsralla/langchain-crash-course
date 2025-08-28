from json import load
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableSequence, RunnableBranch
from typing import Type

from numpy import negative
from torch import negative_


load_dotenv()
model = ChatOpenAI(model="openai/gpt-oss-20b", base_url="https://openrouter.ai/api/v1")

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","You are product reviews reviewer"),
        ("human","Classify the sentiment of this feedback as positive, negative, neutral, or escalate {feedback}.")
    ]
)

positive_feed_back_template = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant"),
        ("human", "Generate a thanks message for the user for his positive feedback, {feedback}")
    ]
)

negative_feed_back_template = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant"),
        ("human", "Generate a sorry message for the user for his negative feedback, {feedback}")
    ]
)   

neutral_feed_back_template = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant"),
        ("human", "Generate a  message for the user asking him for more details about his neutral feedback, {feedback}")
    ]
)

escalate_feed_back_template = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant"),
        ("human", "Generate a message to escalate this feedback to a human agent, {feedback}")
    ]
)

chain = RunnableBranch(
    (
        lambda x: "positive" in x.lower(),
        positive_feed_back_template | model | StrOutputParser(),
    ),
    (
        lambda x: "negative" in x.lower(),
        negative_feed_back_template | model | StrOutputParser(),
    ),
    (
        lambda x: "neutral" in x.lower(),
        neutral_feed_back_template | model | StrOutputParser(),
    ),
    
    escalate_feed_back_template | model | StrOutputParser()
)

classify_chain = prompt_template | model | StrOutputParser()
main_chain = classify_chain | chain 

result = main_chain.invoke({"feedback": "I am not sure about the product yet. can you tell me more about it's features."})
print(result)

