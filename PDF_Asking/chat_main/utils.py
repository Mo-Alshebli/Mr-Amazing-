import pinecone
import openai
import streamlit as st
from langchain.embeddings.openai import OpenAIEmbeddings
from dotenv import load_dotenv

# Set up your OpenAI API key
load_dotenv()
pinecone.init(api_key="", environment="")

# Define the name for your Pinecone index
index_name = 'chat'


# Embed the query using GPT-3.5-turbo


def find_match(input, model):
    embeddings = OpenAIEmbeddings(model=model)
    embedding = embeddings.embed_query(input)
    pinecone_index = pinecone.Index(index_name)
    response = pinecone_index.query(
        vector=embedding,
        top_k=2,
        # include_values=True,
        includeMetadata=True
    )
    return response['matches'][0]['metadata']['text'] + "\n" + response['matches'][1]['metadata']['text']


def query_refiner(conversation, query, model):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user",
             "content": f"بالنظر إلى استعلام المستخدم وسجل المحادثة قم بإعادة صياغة السؤال الى افضل طريقة  هذا السؤال "
                        f"{query}:"
                        f" والنص السابق التابع للمحادثة هو { conversation}"
                        f"قم بضياغة السؤال بحيث يكون سهل ومن نفس البيانات "},
        ],
        temperature=0.7,
        max_tokens=232,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    refined_query = response.choices[0].message.content

    return refined_query


def get_conversation_string():
    conversation_string = ""
    for i in range(len(st.session_state['responses']) - 1):
        conversation_string += "Human: " + st.session_state['requests'][i] + "\n"
        conversation_string += "Bot: " + st.session_state['responses'][i + 1] + "\n"
    return conversation_string
