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
api_key = os.getenv(str(llm_name)+"_API_KEY")
model_name = os.getenv(str(llm_name)+"_MODEL_NAME")

llm= get_model(llm_name,model_name,api_key);

chats = [] #Chat conversation history


chats.append(SystemMessage(content="You are an AI Assistant"))

while True:
    user_query= input("You:>")
    if user_query.lower() == "exit":
        break;
    chats.append(HumanMessage(content=user_query))

    result= llm.invoke(chats)
    response = result.content
    chats.append(AIMessage(content=response))

    print(f"AI :> {response}")

print("--- Message History ---")
print(chats)

