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

#from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

# # chat_model = ChatOpenAI(openai_api_key=api_key)

# # result = chat_model.invoke('Hi')

# # print(result)

# from langchain_core.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI

# llm = ChatOpenAI(openai_api_key=api_key)

# ad_body, skills_lst = [], []

# llm_input = [ad_body, skills_lst]

# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are world class technical documentation writer."),
#     ("user", "{input}")
# ])

# chain = prompt | llm

# result = chain.invoke({"input": "how can langsmith help with testing?"})

# print(result)


from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import json

chat_llm = ChatOpenAI(temperature=0.0)

template_string = """You are a master branding consulatant who specializes in naming brands. \
You come up with catchy and memorable brand names.

Take the brand description below delimited by triple backticks and use it to create the name for a brand.

brand description: ```{brand_description}```

then based on the description and you hot new brand name give the brand a score 1-10 for how likely it is to succeed.

Format the output as JSON with the following keys:
brand_name
likelihood_of_success
reasoning
"""

prompt_template = ChatPromptTemplate.from_template(template_string)

# print(prompt_template.messages[0].prompt)

branding_messages = prompt_template.format_messages(brand_description="a cool hip new sneaker brand aimed at rich kids")

# print(branding_messages)

consultant_response = chat_llm(branding_messages)

print(type(consultant_response.content))

rjs = json.loads(consultant_response.content)

print(rjs)