from google import genai
from dotenv import load_dotenv # To make content of the .env file available

load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is the square root of 49",
)

print(response.text)