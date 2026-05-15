from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv();

apiEndpoint = os.getenv("apiEndpoint")
apiKey = os.getenv("apiKey")

systemPrompt = "SYSTEM: You are a large language model called SchoolSafeAI. Your role is to assist students Socratically by guiding them with questions, simple explainations, and helpful advice. You are not allowed to give direct answers, use or make references to offensive language or media, or lie about having information that you do not. Reply in concise, helpful, and respectful, and simple language. Try to limit responses to 2~3 sentences. | PREVIOUS RESPONSES: "

"""
client = OllamaFreeAPI()

def newPrompt(userPrompt, history):
    if len(history) > 10:
        history = history[-10:]

    totalPrompt= systemPrompt + " ".join(history) + " | USER: " + userPrompt

    print(totalPrompt)

    response = client.chat (
        model="llama3.2:3b",
        prompt=totalPrompt,
        temperature=0.5
    )
    return response;
"""
# This was a legacy api feature. It won't work.

client = OpenAI(
  base_url= apiEndpoint,
  api_key= apiKey,
)

def OpenAICall(userPrompt, history):
    if len(history) > 15:
        history = history[-15:]
    totalPrompt = systemPrompt + " ".join(history) + " | USER: " + userPrompt
    print(totalPrompt)
    AIresponse = client.chat.completions.create(
        model="nvidia/nemotron-3-super-120b-a12b:free",
        messages=[
            {
                "role": "user",
                "content": totalPrompt
            }
        ],
    extra_body={"reasoning": {"enabled": False}}
    )
    
    return AIresponse
