from crewai import LLM
import os
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()


def get_langchain_chat_llm(model_name="gemini"):
    if model_name == "groq":
        api_key = os.getenv("GROQ_API_KEY")
        return ChatGroq(model=model_name,api_key=api_key)
    elif model_name == "gemini":
        api_key = os.getenv("GEMINI_API_KEY")
        return ChatGoogleGenerativeAI(model="gemini-2.0-flash-001",api_key=api_key,temperature=0.1)
    else:
        raise ValueError(f"Model {model_name} not supported")

#create a groq llm
def get_groq_llm(api_key=os.getenv("GROQ_API_KEY")):
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable is not set. Please add it to your .env file.")
    
    llm=LLM(model="groq/llama-3.1-8b-instant",api_key=api_key) 

    return llm


def get_gemini_llm(api_key=os.getenv("GEMINI_API_KEY")):
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is not set. Please add it to your .env file.")
    
    llm=LLM(model="gemini/gemini-2.0-flash-001",api_key=api_key) 

    return llm
