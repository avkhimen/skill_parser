# import numpy as np
# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# import os
# from dotenv import load_dotenv
# from langchain_core.output_parsers import StrOutputParser

# load_dotenv()

# output_parser = StrOutputParser()

# print(os.getenv('OPENAI_API_KEY'))

# llm = ChatOpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'))

# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are world class technical documentation writer."),
#     ("user", "{input}")
# ])

# chain = prompt | llm | output_parser

# chain.invoke({"input": "how can langsmith help with testing?"})

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

# chat_model = ChatOpenAI(openai_api_key=api_key)

# result = chat_model.invoke('Hi')

# print(result)

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(openai_api_key=api_key)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])

chain = prompt | llm

result = chain.invoke({"input": "how can langsmith help with testing?"})

print(result)