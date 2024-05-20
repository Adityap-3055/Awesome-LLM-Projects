from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st 
import os
from dotenv import load_dotenv


os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

## Langsmith Tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY") # this tells where all the monotoring is going to be stored i.e. langchain dashboard


## Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpfull assistant, please respond to the user queries"),
        ("user", "Question:{question}")
    ]
)


## Streamlit framework
st.title('Langchain Demo with open AI')
input_text = st.text_input("Search the topic you want.")


## openAI LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")


ouptput_parser = StrOutputParser()

chain = prompt|llm|ouptput_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))