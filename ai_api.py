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

    print(f"Calling OpenAI, resume length: {len(resume_text) if resume_text else 0}")

    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            input=full_prompt,
            store=False,
        )
    except Exception as e:
        print(f"OpenAI call failed: {e}")
        raise

    print(f"Raw OpenAI output: {response.output_text!r}")
    return response.output_text