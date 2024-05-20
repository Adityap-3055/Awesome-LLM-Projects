from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv() ## helps to initialize all the environment variable

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)


add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

## first model
model = ChatOpenAI()

## second model ollama llama2
llm = Ollama(model="llama2")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 70 words")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} with 40 words")

add_routes(
    app,
    prompt1|model,
    path="/essay"
)

add_routes(
    app,
    prompt2|model,
    path="/poem"
)


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
