import os 
from openai import OpenAI
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# Define base URL for Gemini API with OpenAI client 
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

# Get the Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Create an OpenAI client with Gemini API key
gemini_client = OpenAI(base_url=GEMINI_BASE_URL,
                       api_key=GEMINI_API_KEY)
response = gemini_client.chat.completions.create(
    model="gemini-2.5-flash-preview-05-20",
    messages=[{"role":"user", "content":"What is 2+2"}]
)

print(response.choices[0].message.content)