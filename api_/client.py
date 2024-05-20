import requests
import streamlit as st

def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke",
                             json={'input':{'topic': input_text}})
    
    return response.json()['output']['content']


def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke",
                             json={'input':{'topic': input_text}})
    
    return response.json()['output']['content']


st.title('Lanchain API with OpenAI and Ollama')

input_text=st.text_input("(OpenAI) Write an essay on")
if input_text:
    st.write(get_openai_response(input_text))


input_text1=st.text_input("(Ollama) Write a poem on")

if input_text1:
    st.write(get_ollama_response(input_text1))

