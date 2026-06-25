from dotenv import load_dotenv
import os
from openai import OpenAI
import prompt

load_dotenv()
api_key = os.getenv("API_KEY")
client = OpenAI(api_key=api_key)

def get_booth_recommendations(resume_text):
    full_prompt = prompt.promptText.format(
        user_resume_data=resume_text,
        company_data=prompt.company_data,
    )

    response = client.responses.create(
        model="gpt-4o-mini",
        input=full_prompt,
        store=False,
    )

    return response.output_text