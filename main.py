import numpy as np
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv('OPENAI_API_KEY'))

llm = ChatOpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'))

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])