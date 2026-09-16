# from langchain_openrouter import ChatOpenRouter
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatOpenRouter(model="nvidia/nemotron-3-super-120b-a12b:free")
# result = model.invoke("Age of him?")

# print(result.content)



# from langchain_openai import OpenAIEmbeddings
# from dotenv import load_dotenv
# import os   
# load_dotenv()

# embedding = OpenAIEmbeddings(
#     model="nvidia/nemotron-3-embed-1b:free",
#     base_url="https://openrouter.ai/api/v1",
#     api_key=os.getenv("OPENROUTER_API_KEY"),
#     check_embedding_ctx_length=False,
#     encoding_format="float"
# )

# documents = [
#     "Delhi is the capital of India",
#     "Kolkata is the capital of West Bengal",
#     "Paris is the capital of France"
# ]

# result = embedding.embed_documents(documents)

# print(result)
# 

# print(result.content)

# from langchain_openai import OpenAIEmbeddings
# from dotenv import load_dotenv
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np
# import os   
# load_dotenv()

# embedding = OpenAIEmbeddings(
#     model="nvidia/nemotron-3-embed-1b:free",
#     base_url="https://openrouter.ai/api/v1",
#     api_key=os.getenv("OPENROUTER_API_KEY"),
#     check_embedding_ctx_length=False,
#     dimensions=2048,
#     model_kwargs={
#         "encoding_format": "float"
#     }
# )
# documents = [ 
#     "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
#     "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
#     "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
#     "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
#     "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
# ]

# query = 'Tell me about Virat Kohli'

# doc_embedding = embedding.embed_documents(documents)
# query_embedding = embedding.embed_query(query)

# scores = cosine_similarity([query_embedding], doc_embedding)[0] #to get only list instead of a 2d list

# index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]  # x[1] means on the basis of second element of the lsit and [-1] to extract the last in the asc order
# print(query)
# print(documents[index])
# print("Similarity score : ",score)


#prompt

# from langchain_openrouter import ChatOpenRouter
# import streamlit as st
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate,load_prompt
# # template = PromptTemplate(
# #     template ="""
# #     Please analyze the performance and career of the cricket player named "{chat_input}" with the following specifications:
# # Explanation Style: {style_input}
# # Explanation Length: {length_input}

# # 1. Statistical & Technical Details:
# # - Include relevant career statistics, strike rates, or bowling/batting averages if available.
# # - Explain tactical concepts (like technique, captaincy formulas, or swing physics) using simple, intuitive code snippets or breakdown matrices where applicable.

# # 2. Analogies:
# # - Use relatable analogies to simplify complex playing styles or career milestones.

# # If certain information or data is not available for this player, respond with: "Insufficient information available" instead of guessing.
# # Ensure the analysis is clear, accurate, and aligned with the provided style and length.
# # """,
# # input_variables=["chat_input", "style_input", "length_input"]
# # )

# # template.save('template.json')

# load_dotenv()
# model = ChatOpenRouter(model="openrouter/free")
# st.header("Chat with AI")

# # user_input = st.text("Enter your question here")
# chat_input = st.selectbox( "Select Player Name", ["Virat Kohli","Rohit Sharma", "MS Dhoni", "Bhuvi"] )

# style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Fun"] )

# length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium(3-5 paragraphs)", "Long (detailed explanation)"] )

# template = load_prompt('template.json') # benefit over f string


# if st.button("Send"):
#     chain = template | model  # benefit over f string

#     result = chain.invoke({
#         'chat_input':chat_input,
#         'style_input':style_input,
#         'length_input':length_input
#     })
#     # prompt = template.invoke({
#     #     'chat_input':chat_input,
#     #     'style_input':style_input,
#     #     'length_input':length_input
#     # })
#     # result = model.invoke(prompt)
#     st.write(result.content)

# Chat Bot
# from langchain_openrouter import ChatOpenRouter
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatOpenRouter(model="openrouter/free")
# chat_history = []
# while True:
#     user_input = input('You: ')
#     chat_history.append(user_input)
#     if user_input == 'exit':
#         break
#     result = model.invoke(chat_history)
#     chat_history.append(result.content)
#     print('Ai: ',result.content)
# print(chat_history)

# Chat bot with Different Messages types 

# from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
# from langchain_openrouter import ChatOpenRouter
# from dotenv import load_dotenv
# load_dotenv()

# model = ChatOpenRouter(model="openrouter/free")

# chat_history = [
#     SystemMessage(content='You are a helpful assistant')
# ]
# while True:
#     user_input = input('You: ')
#     chat_history.append(HumanMessage(content=user_input))
#     if user_input == 'exit':
#         break
#     result = model.invoke(chat_history)
#     chat_history.append(AIMessage(content=result.content))
#     print('Ai: ',result.content)
# print(chat_history)
# # result = model.invoke(messages)
# # messages.append(AIMessage(content='result.content'))

# # print(messages)

# chatbot with chat prompt template
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_openrouter import ChatOpenRouter
# from dotenv import load_dotenv
# load_dotenv()

# chat_template = ChatPromptTemplate([
#     ('system','You are a helpful {domain} expert'),
#     ('human','Explain in simple terms, what is {topic}')
    
# ])
# prompt = chat_template.invoke({'domain':'cricket','topic':'Bat'})

# print(prompt)

#Message Placeholder 
# from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

# chat_template = ChatPromptTemplate([
#     ('system','You are a helpful customer support agent'),
#     MessagesPlaceholder(variable_name='chat_history'),
#     ('human','{query}') 
# ])
# chat_history=[]
# with open('chat_history.txt') as h:
#     chat_history.extend(h.readlines())
# print(chat_history)

# prompt = chat_template.invoke({'chat_history': chat_history, 'query': 'Where is my refund'})

# print(prompt)

# Structured Output 
# using typeddict
# from typing import TypedDict

# class Person(TypedDict):
#     name : str
#     age : int
# new_person: Person = {'name':'Pulkit', 'age':23}

# print(new_person)


# from typing import TypedDict
# from langchain_openrouter import ChatOpenRouter
# from dotenv import load_dotenv

# load_dotenv()
# model = ChatOpenRouter(model="openrouter/free")

# class Review(TypedDict):
#     summary : str
#     sentiment: str
# structured_model = model.with_structured_output(Review)

# result = structured_model. invoke("""The hardware is great, but the software feels bloated. There are
# too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to
# other brands. Hoping for a software update to fix this.""")

# print(result)
# print(result['summary'])
# print(type(result))

#with structured output typeddict
# from langchain_openrouter import ChatOpenRouter
# from dotenv import load_dotenv
# from typing import TypedDict,Annotated,Optional,Literal

# load_dotenv()
# model = ChatOpenRouter(model="openrouter/free")
                
# # schema
# class Review(TypedDict):
#     key_themes:Annotated[list[str],"Write down all the key themes discusses in the review in a list"]
#     summary :Annotated[str,"A brief summary of the review"]
#     sentiment : Annotated[Literal['Positive','Negative'],"Return sentiment of the review either negative, positive or neutral"]
#     pros:Annotated[Optional[list[str]],"Write down all the pros in the list "]
#     cons:Annotated[Optional[list[str]],"Write down all the cons in the list "]
#     name:Annotated[Optional[str],"Write the Name of the reviewer"]

# structured_model = model.with_structured_output(Review)

# result = structured_model. invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3
# processor makes everything lightning fast-whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily
# lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

# The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me
# away is the 200MP camera-the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x
# actually works well for distant objects, but anything beyond 30x loses quality.

# However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with
# bloatware-why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard
# pill to swallow.

# Pros:
# Insanely powerful processor (great for gaming and productivity)
# Stunning 200MP camera with incredible zoom capabilities
# Long battery life with fast charging
# S-Pen support is unique and useful

# Cons:
# Bulky and heavy-not great for one-handed use
# Bloatware still exists in One UI
# Expensive compared to competitors

# Review done By Pulkit Kalra
# """)

# # print(result)
# print(result['summary'])
# print(result['sentiment'])
# print(result['


#pydantic

# from pydantic import BaseModel
# class Student(BaseModel):
#     name : str

# new_student = {'name':'Pulkit'} # the type is restricted we cannot write 32 in this where as in typeddict this does not throw the error

# student = Student(**new_student) # unpacks this as it is dictionary 
# print(type(student))
# print(student)

# default value 
# from pydantic import BaseModel,EmailStr,Field
# from typing import Optional #optional field 
# class Student(BaseModel):
#     name: str = 'pulkit'
#     age:Optional[int]=None # if no value is given then it should be none
#     email:EmailStr  # built in data validation
#     cgpa:float = Field(gt=0,lt=10, default=5) # with field we can set constraints,default value, example and description

# new_student = {'age':'23','email':'pulkit@gmail.com'} #type conversion on age field that it coerce or type coercing 

# student = Student( ** new_student)
# student_dict = dict(student) #converted into dict to access only age 
# print(student_dict['age'])
# student_json = student.model_dump_json() # to covert to json    

# use of pydantic in mobile review

# from langchain_openrouter import ChatOpenRouter
# from dotenv import load_dotenv
# from typing import TypedDict,Annotated,Optional,Literal
# from pydantic import BaseModel,Field
# load_dotenv()
# model = ChatOpenRouter(model="openrouter/free")
                
# # schema
# class Review(BaseModel):
#     key_themes:list[str] = Field(description ="Write down all the key themes discusses in the review in a list")
#     summary :str= Field(description="A brief summary of the review")
#     sentiment : Literal['Positive','Negative'] = Field(description ="Return sentiment of the review either negative, positive or neutral")
#     pros:Optional[list[str]]= Field(default = None, description ="Write down all the pros in the list ")
#     cons:Optional[list[str]]= Field(default = None, description ="Write down all the cons in the list ")
#     name:Optional[str]= Field(default = None, description ="Write the Name of the reviewer")

# structured_model = model.with_structured_output(Review)

# result = structured_model. invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3
# processor makes everything lightning fast-whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily
# lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

# The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me
# away is the 200MP camera-the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x
# actually works well for distant objects, but anything beyond 30x loses quality.

# However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with
# bloatware-why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard
# pill to swallow.

# Pros:
# Insanely powerful processor (great for gaming and productivity)
# Stunning 200MP camera with incredible zoom capabilities
# Long battery life with fast charging
# S-Pen support is unique and useful

# Cons:
# Bulky and heavy-not great for one-handed use
# Bloatware still exists in One UI
# Expensive compared to competitors

# Review done By Pulkit Kalra
# """)

# # print(result)
# print(result.cons) # it is pydantic object so we can't extract like that 
# # print(result['sentiment']) # it is pydantic object so we can't extract like that 


# Json schema

# from langchain_openrouter import ChatOpenRouter
# from dotenv import load_dotenv
# from typing import TypedDict,Annotated,Optional,Literal
# from pydantic import BaseModel,Field
# load_dotenv()
# model = ChatOpenRouter(model="openrouter/free")
                
# # json schema
# json_schema = {
#   "title": "Review",
#   "type": "object",
#   "properties": {
#     "key_themes": {
#       "type": "array",
#       "items": {
#         "type": "string"
#       },
#       "description": "Write down all the key themes discussed in the review in a list"
#     },
#     "summary": {
#       "type": "string",
#       "description": "A brief summary of the review"
#     },
#     "sentiment": {
#       "type": "string",
#       "enum": ["pos", "neg"], # literal is not used enum is used
#       "description": "Return sentiment of the review either negative or positive"
#     },
#     "pros": {
#       "type": ["array", "null"],
#       "items": {
#         "type": "string"
#       },
#       "description": "Write down all the pros inside a list"
#     },
#     "cons": {
#       "type": ["array", "null"],
#       "items": {
#         "type": "string"
#       },
#       "description": "Write down all the cons inside a list"
#     },
#     "name": {
#       "type": ["string", "null"],
#       "description": "Write the name of the reviewer"
#     }
#   },
#   "required": ["key_themes", "summary", "sentiment"]
# }


# structured_model = model.with_structured_output(json_schema)

# result = structured_model. invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3
# processor makes everything lightning fast-whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily
# lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

# The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me
# away is the 200MP camera-the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x
# actually works well for distant objects, but anything beyond 30x loses quality.

# However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with
# bloatware-why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard
# pill to swallow.

# Pros:
# Insanely powerful processor (great for gaming and productivity)
# Stunning 200MP camera with incredible zoom capabilities
# Long battery life with fast charging
# S-Pen support is unique and useful

# Cons:
# Bulky and heavy-not great for one-handed use
# Bloatware still exists in One UI
# Expensive compared to competitors

# Review done By Pulkit Kalra
# """)

# # print(result)
# # print(result.cons) # it is pydantic object so we can't extract like that 
# print(result['cons']) # it is dict so we extract like that 



# Output Parsers without stroutputparser

# from langchain_openrouter import ChatOpenRouter
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate

# load_dotenv()
# model = ChatOpenRouter(model="openrouter/free")

# template1 = PromptTemplate(
#     template ='Write a detailed report on {topic}',
#     input_variables=['topic']
# )
# template2 = PromptTemplate(
#     template ='Write a 5 line summary on the following text. /n {text}',
#     input_variables=['text']
# )
# prompt1 = template1.invoke({'topic':'black hole'})
# result = model.invoke(prompt1)
# prompt2 = template2.invoke({'text':result.content})
# result1= model.invoke(prompt2)

# print(result1.content)

# with output parser
# from langchain_openrouter import ChatOpenRouter
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# load_dotenv()
# model = ChatOpenRouter(model="openrouter/free")

# template1 = PromptTemplate(
#     template ='Write a detailed report on {topic}',
#     input_variables=['topic']
# )
# template2 = PromptTemplate(
#     template ='Write a 5 line summary on the following text. /n {text}',
#     input_variables=['text']
# )

# parser = StrOutputParser()
# chain = template1 | model | parser | template2 | model | parser
# result = chain.invoke({'topic':'Black hole'})
# print(result)

# with JSON ouput parser
# from langchain_openrouter import ChatOpenRouter
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import JsonOutputParser

# load_dotenv()
# model = ChatOpenRouter(model="openrouter/free")

# parser = JsonOutputParser()

# template1 = PromptTemplate(
#     template ='Give me the name, age and city of a fictional person \n {format_instruction}',
#     input_variables=[],
#     partial_variables={'format_instruction': parser.get_format_instructions()} # it fills before the runtime and gives the instruction that in which format we want given by parser 
# )

# chain = template1 | model | parser  # with chains 

# output = chain.invoke({}) # as no input variables are there so we send a blank dict

# # prompt = template1.format()

# # result = model.invoke(prompt)

# # output = parser.parse(result.content)
# print(output['name'])
# print(type(output))


# StructuredOutput Parser now outdated 

# from langchain_openrouter import ChatOpenRouter
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StructuredOutputParser,ResponseSchema


# load_dotenv()
# model = ChatOpenRouter(model="openrouter/free")

# schema = [
#     ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
#     ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
#     ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
# ]
# parser = StructuredOutputParser. from_response_schemas (schema)

# template = PromptTemplate(
# template='Give 3 fact about {topic} \n {format_instruction} ',
# input_variables=['topic'],
# partial_variables={'format_instruction':parser.get_format_instructions()}
# )
# chain = template | model | parser

# result = chain.invoke({'topic':'black hole'})

# print(result)

#Pydantic output parser 
# from langchain_openrouter import ChatOpenRouter
# from dotenv import load_dotenv
# from pydantic import BaseModel,Field
# from langchain_core.output_parsers import PydanticOutputParser
# from langchain_core.prompts import PromptTemplate

# load_dotenv()
# model = ChatOpenRouter(model="openrouter/free")

# class Person(BaseModel):
#     name: str = Field(description='Name of the person')
#     age: int = Field(gt=18,description='Age of the person')
#     city: str = Field(description='Name of the city the person belongs to')

# parser = PydanticOutputParser(pydantic_object=Person)
# template = PromptTemplate(
#     template ='Generate the name,age and city of a fictional {place} person \n {format_instruction}',
#     input_variables=['place'],
#     partial_variables={'format_instruction':parser.get_format_instructions()}
# )

# chain = template | model | parser

# output = chain.invoke({'place':'Russian'})

# print(output)


# Chains

# from langchain_openrouter import ChatOpenRouter
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# load_dotenv()
# model = ChatOpenRouter(model="openrouter/free")

# prompt = PromptTemplate(
#     template = 'Generate 5 interesting fact about {topic}',
#     input_variables=['topic']
# )
# parser = StrOutputParser()
# chain = prompt|model|parser

# result = chain.invoke({'topic':'cricket'})
# print(result)

# chain.get_graph().print_ascii()

#Sequential Chain 

# from langchain_openrouter import ChatOpenRouter
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# load_dotenv()
# model = ChatOpenRouter(model="openrouter/free")

# template1 = PromptTemplate(
#     template ='Write a detailed report on {topic}',
#     input_variables=['topic']
# )
# template2 = PromptTemplate(
#     template ='Write a 5 line summary on the following text. /n {text}',
#     input_variables=['text']
# )

# parser = StrOutputParser()
# chain = template1 | model | parser | template2 | model | parser
# result = chain.invoke({'topic':'Unemployement in India'})
# print(result)
# chain.get_graph().print_ascii()

# Parallel chain

# from langchain_openrouter import ChatOpenRouter
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import RunnableParallel  # parallely we can excute multiple chains

# load_dotenv()
# model1 = ChatOpenRouter(model="openrouter/free")
# model2 = ChatOpenRouter(model="openrouter/free")

# prompt1 = PromptTemplate(
#     template='Generate short and simple notes from the following text \n {text}',
#     input_variables=['text']
# )

# prompt2 = PromptTemplate(
#     template='Generate 5 short question and answer from the following text \n {text}',
#     input_variables=['text']
# )

# prompt3 = PromptTemplate(
#     template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz ->{quiz}',
#     input_variables=['notes', 'quiz']
# )
# parser = StrOutputParser()

# parallel_chain = RunnableParallel({
#     'notes': prompt1 | model1 | parser,
#     'quiz':prompt2 | model2 | parser
# })

# merge_chain = prompt3 | model1 | parser

# chain = parallel_chain | merge_chain

# text = """Support vector machines (SVMs) are a set of supervised learning methods used for classification,
# regression and outliers detection.

# The advantages of support vector machines are:

# · Effective in high dimensional spaces.
# . Still effective in cases where number of dimensions is greater than the number of samples.
# . Uses a subset of training points in the decision function (called support vectors), so it is also memory
# efficient.

# . Versatile: different Kernel functions can be specified for the decision function. Common kernels are
# provided, but it is also possible to specify custom kernels.

# The disadvantages of support vector machines include:

# . If the number of features is much greater then the number of samples, avoid over-fitting in choosing
# Kernel functions and regularization term is crucial.
# . SVMs do not directly provide probability estimates, these are calculated using an ekpensive five-fold
# cross-validation (see Scores and probabilities, below).

# The support vector machines in scikit-learn support both dense ( numpy.ndarray and convertible to that by
# numpy.asarray ) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make
# predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered
# numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64"""

# result = chain.invoke({'text':text})
# # print(result)
# chain.get_graph().print_ascii()

#conditional chain
# from langchain_openrouter import ChatOpenRouter
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
# from langchain_core.runnables import RunnableBranch,RunnableLambda  # if and else in chains and lamda makes any lambda function into runnable so we can make it in a chain
# from pydantic import BaseModel,Field
# from typing import Literal

# load_dotenv()
# model = ChatOpenRouter(model="openrouter/free")
# parser1 = StrOutputParser()

# class feedback(BaseModel):
#     sentiment:Literal['positive','negative'] = Field(description='Give the sentiment of the feedback')
# parser2 = PydanticOutputParser(pydantic_object=feedback)

# prompt1 = PromptTemplate(
#     template='Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}',
#     input_variables=['feedback'],
#     partial_variables={'format_instruction':parser2.get_format_instructions()}
# )   
# classifier_chain = prompt1 | model | parser2

# prompt2 = PromptTemplate(
#     template='Write an appropriate response to this positive feedback\n {feedback}',
#     input_variables=['feedback']
# )   
# prompt3 = PromptTemplate(
#     template='Write an appropriate response to this negative feedback\n {feedback}',
#     input_variables=['feedback']
# )  

# chain_branch = RunnableBranch(
#     (lambda x:x.sentiment == 'positive', prompt2 | model | parser1),
#     (lambda x:x.sentiment == 'negative', prompt3 | model | parser1),
#     RunnableLambda(lambda x:"could not find sentiment")
# )
# chain = classifier_chain | chain_branch

# result = chain.invoke({'feedback':'This is a wonderful smartphone'})
# chain.get_graph().print_ascii()


# Runnables 

from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence 

load_dotenv()
model = ChatOpenRouter(model="openrouter/free")

prompt1 = PromptTemplate(
    template = 'Write a joke about {topic}',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template = 'Explain the following joke {text}',
    input_variables=['text']
)
parser = StrOutputParser()

chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)

print(chain.invoke({'topic':'AI'}))