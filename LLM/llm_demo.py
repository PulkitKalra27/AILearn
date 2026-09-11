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
# from langchain_core.prompts import PromptTemplate

# load_dotenv()
# model = ChatOpenRouter(model="openrouter/free")
# st.header("Chat with AI")

# # user_input = st.text("Enter your question here")
# chat_input = st.selectbox( "Select Player Name", ["Virat Kohli","Rohit Sharma", "MS Dhoni", "Bhuvi"] )

# style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Fun"] )

# length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium(3-5 paragraphs)", "Long (detailed explanation)"] )

# template = PromptTemplate(
#     template ="""
#     Please analyze the performance and career of the cricket player named "{chat_input}" with the following specifications:
# Explanation Style: {style_input}
# Explanation Length: {length_input}

# 1. Statistical & Technical Details:
# - Include relevant career statistics, strike rates, or bowling/batting averages if available.
# - Explain tactical concepts (like technique, captaincy formulas, or swing physics) using simple, intuitive code snippets or breakdown matrices where applicable.

# 2. Analogies:
# - Use relatable analogies to simplify complex playing styles or career milestones.

# If certain information or data is not available for this player, respond with: "Insufficient information available" instead of guessing.
# Ensure the analysis is clear, accurate, and aligned with the provided style and length.
# """,
# input_variables=["chat_input", "style_input", "length_input"]
# )

# prompt = template.invoke({
#     'chat_input':chat_input,
#     'style_input':style_input,
#     'length_input':length_input
# })

# if st.button("Send"):
#     result = model.invoke(prompt)
#     st.write(result.content)


# 

# print(result.content)

# Structured Output 
# using typeddict
# from typing import TypedDict

# class Person(TypedDict):
#     name : str
#     age : int
# new_person: Person = {'name':'Pulkit', 'age':23}

# print(new_person)

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
# print(result['name'])

#pydantic

from pydantic import BaseModel
class Student(BaseModel):
    name : str

new_student = {'name':'Pulkit'} # the type is restricted we cannot write 32 in this where as in typeddict this does not throw the error

student = Student(**new_student)

print(student)