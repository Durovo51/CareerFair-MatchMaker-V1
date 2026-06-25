from dotenv import load_dotenv
import os
from openai import OpenAI
import prompt

load_dotenv()
api_key = os.getenv("API_KEY")

client = OpenAI(api_key=api_key)

response = client.responses.create(
  model="gpt-4o-mini",
  input=prompt.promptText,
  store=False,
)

print(response.output_text)