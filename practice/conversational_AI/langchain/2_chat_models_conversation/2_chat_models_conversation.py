from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv # To make content of the .env file available

load_dotenv()


def get_model(llm_name:str,model_name: str, api_key: str):
    print("Inside function ",llm_name)
    if llm_name == "GEMINI":
        print("Returning Gemini")
        return ChatGoogleGenerativeAI(model=model_name,google_api_key=api_key, temperature=0.8)
    else:
        return None
    
import os

llm_name = os.getenv("LLM_NAME")
print(llm_name)
api_key = os.getenv(str(llm_name)+"_API_KEY")
print(api_key)
model_name = os.getenv(str(llm_name)+"_MODEL_NAME")
print(model_name)

llm= get_model(llm_name,model_name,api_key);

messages = [
    SystemMessage("You are an expert in social media content strategy, and you always respond in a very energetic, brief, and bulleted list."),
    AIMessage("Here's a quick tip! * Use a trending audio track."),
    HumanMessage("Give a short tip to create engaging post on Instagram")
]

result = llm.invoke(messages)

print(result.content)
