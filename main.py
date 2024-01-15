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

chat_llm = ChatOpenAI(name='gpt-4')

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

print('---------------------------------------')

from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser

schema = ResponseSchema(name="skill_competencies",
                        description="This is the competencies of the skills in python list format")

response_schemas = [schema]

output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

format_instructions = output_parser.get_format_instructions()

print(format_instructions)

template_string = """You are a master skill evaluator who evaluates skills from the job ads who \
decides whether the skill required is junior in competency, intermediate, or senior.

Take the job ad from the job_ad input and the skills list from the skill_list input.

brand description: ```{job_ad}``` ```{skills_list}```

then based on the job ad and the skills input list give the competency required for each skill based on the job ad.

{format_instructions}
"""

prompt = ChatPromptTemplate.from_template(template=template_string)

job_ad_description = """
Senior Mechanical Engineer - ( 230004T3 )

Description

Stantec Buildings is on a mission to become the world’s leading integrated design practice. Our architects, engineers, interior designers, sustainability specialists, and technologists are passionate about the power of design. We take an innovative, collaborative approach to projects, sharing a common belief that sustainable design for the built environment can make the world a better place for future generations. Join us and design your place with Stantec.

Your Opportunity

Stantec Buildings is a group of interdisciplinary consultants that work collaboratively to deliver innovative and sustainable projects safely. Your role as a Senior Mechanical Engineer and contributor on our professional consulting services team is to work independently to execute large projects of high complexity across various sectors and locations in Western and Northern Canada. You will be a leader of a team or project through all phases of a project lifecycle. You will also be responsible for developing and implementing an engineering discipline group equipped with up-to-date engineering and design tools and innovations, technical and supervisory capabilities and operating procedures to successfully and efficiently execute projects and consulting services resulting in client satisfaction and on-time delivery. You will be based out of the Edmonton, AB office.

Your Key Responsibilities
• Responsible for a diverse portfolio of projects in scale and complexity and ensuring projects are delivered on budget and schedule while driving innovation, technical excellence and quality control and assurance.
• Evaluates, selects, specifies, and engineers all mechanical engineered systems or products for a project.
• Act as technical advisor on more unusual and complex issues and guide staff on solutions
• Engages in the development of a design through sketches, electronic models, diagrams, and other visual formats.
• Utilizes BIM technologies in development of three dimensional models of building’s mechanical systems and provides markups for junior engineers/ designers.
• Prepares, develops and revises mechanical documentation in various project phases including reports, site plans, floor plans, diagrams, and details.
• Acts as Prime Consultant and lead project manager and contract execution for mechanical projects and lead, direct and coordinate with all other consultants
• Leads project coordination meetings with internal team members and/or external consultants, owner and contractor, sub-contractors, and vendors.
• Participates in client project requirement meetings, value analysis, and basic cost estimating.
• Leads the preparation and coordination of the project specifications with construction documents.
• Provides direct supervision to assigned staff; develop staff skills and abilities by providing guidance and mentoring through effective communication to strengthen technical abilities and work ethic
• Participates in constructability review.
• Conducts quality assurance and quality control on own projects and projects of peers.
• Assists in the development of new standards and specifications for the mechanical group.
• Develops project scope, budgets, and design approach for all size projects.
• Develops and contributes to proposals for diverse types and scales of projects including creation of fee estimates, scope of work and work plans.
• Oversees and manages multiple projects.
• Develops strong client relationships through proactive business development and marketing efforts as well as through exceptional delivery of projects and associated deliverables.
• Work collaboratively to support the Alberta Building Engineering Team and wider North American Building Engineering Team to develop and implement programs and procedures affecting Mechanical Engineering.

Qualifications

Your Capabilities and Credentials
• In depth knowledge, interpretation, and application of the mechanical and/or plumbing codes, energy codes, ASHRAE standards, and other building codes and standards.
• Strong understanding of all building mechanical systems including HVAC, Plumbing, Fire Protection and Building Controls.
• Strong understanding of all phases of project document production and the relationship between drawings and specifications.
• Strong knowledge of mechanical systems, means and methods, materials, and industry standards.
• Strong knowledge of high performance and sustainable building practices with experience designing for LEED certified and / or Net Zero Carbon and Energy buildings.
• Ability to lead one or more teams through all phases of project document production with knowledge of professional services procurement processes including both Consultant and Construction Contracts
• Checks the work of others for accuracy and completeness and manages time to meet project budget and schedule.
• Participates and collaborates in project team setting and to engage in creative and critical thought.
• Demonstrates creativity, foresight and mature engineering judgment in anticipating and solving problems
• Thorough understanding of mechanical engineering concepts and ability to communicate ideas to others.
• Strong presentation and interview skills.
• Ability to qualify for security clearance based on client requirements, nationally and internationally.
• Ability to travel as required for projects such as client meetings and site reviews
• Excellent skills in Microsoft Office Suite, Revit, AutoCAD, Bluebeam, and Adobe Acrobat. Experience with Newforma, Integrated Environmental Solutions (IES), and Trane Trace would be considered an asset.

Education and Experience
• Bachelor’s degree or equivalent in Engineering & Licensed Professional Engineer in Alberta.
• Minimum of 10 years of experience.
• LEED Green Associate or LEED AP BD C preferred. Experience working on large healthcare, laboratory / research or sports and recreation projects is considered an asset.

Typical office environment working with computers and remaining sedentary for long periods of time. Field work may include exposure to the elements including inclement weather.

This description is not a comprehensive listing of activities, duties or responsibilities that may be required of the employee and other duties, responsibilities and activities may be assigned or may be changed at any time with or without notice.

Stantec is a place where the best and brightest come to build on each other's talents, do exciting work, and make an impact on the world around us. Join us and redefine your personal best. #DesignYourPlace

Benefits Summary: Regular full-time and part-time employees will have access to health, dental, and vision plans, a well-being program, health care spending account, wellness spending accounts, group registered retirement savings plan, employee stock purchase program, group tax-free savings account, life and accidental death & dismemberment (AD&D) insurance, short-term/long-term disability plans, emergency travel benefits, tuition reimbursement, professional membership fee coverage, and paid time off.

Temporary/casual employees will have access to group registered retirement savings plan, employee stock purchase program, and group tax-free savings account.

The benefits information listed above may not apply to union positions because benefits for such positions are governed by applicable collective bargaining agreements.

Primary Location : Canada-Alberta-Edmonton

Work Locations :

Edmonton AB

Organization : BC-1153 Buildings-CA Alberta

Employee Status : Regular

Job Level : Individual Contributor

Travel : Yes, 10 % of the Time

Schedule : Full-time

Job Posting : Nov 24, 2023, 12:52:15 PM

Req ID: 230004T3

Stantec provides equal employment opportunities to all qualified employees and applicants for future and current employment and prohibit discrimination on the grounds of race, color, religion, sex, national origin, age, marital status, genetic information, disability, protected veteran status, sexual orientation, gender identity or gender expression. We prohibit discrimination in decisions concerning recruitment, hiring, referral, promotion, compensation, fringe benefits, job training, terminations or any other condition of employment. Stantec is in compliance with local, state and federal laws and regulations and ensures equitable opportunities in all aspects of employment. EEO including Disability/Protected Veterans
"""

messages = prompt.format_messages(job_ad=job_ad_description,
                                  skills_list="[mechanical engineering, drafting, HVAC, plumbing codes]",
                                  format_instructions=format_instructions)

print(messages)

print(messages[0].content)

response = chat_llm(messages)

print(response)

response_as_dict = output_parser.parse(response.content)

print(response_as_dict)
     