from networkx import prominent_group
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.messages import AIMessage, HumanMessage


prompt_text = "Tell me a joke about {topic}"
template_prompt = PromptTemplate.from_template(prompt_text)
prompt = template_prompt.invoke({"topic": "cats"})
print(prompt)

# CREATE PROMPT WITH MULTIPLE PLACEHOLRDERS
prompt_text = "You are a helpful assistant, tell me a {adjective} story about {topic}."
template_prompt = PromptTemplate.from_template(prompt_text)
prompt = template_prompt.invoke({"adjective":"funny", "topic": "engineers"})
print(prompt)

# CREATING PROMPT WITH Human messages
messages = [
    ("system", "You are a comedian assistant who tells jokes about {topic}."),
    ("human", "Can you tell me {jokes_count} joke about cats?")
]
template_prompt = ChatPromptTemplate.from_messages(messages)
prompt = template_prompt.invoke({"jokes_count": 3, "topic": "cats"})
print(prompt)

# EXTRA
messages = [
    ("system", "you are  a comedian assistant who tells jokes about {topic}."),
    HumanMessage(content="Can you tell me jokes about it?") # you can't use placeholders here
]
prompt_template = ChatPromptTemplate.from_messages(messages=messages)
prompt = prompt_template.invoke({"topic": "dogs"})
print(prompt)

# example below will cause an error
# messages = [
#     ("system", "you are  a comedian assistant who tells jokes about {topic}."),
#     HumanMessage(content="Can you tell me {jokes_count} jokes about {topic}?")
# ]
# prompt_template = ChatPromptTemplate.from_messages(messages=messages)
# prompt = prompt_template.invoke({"jokes_count": 3, "topic": "dogs"})
# print(prompt)
