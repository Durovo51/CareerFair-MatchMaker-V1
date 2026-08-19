import re
from flask import Flask, render_template, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
import ai_api

app = Flask(__name__)

NO_MATCH_MESSAGE = "You don't have any matches at this career fair."


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/match', methods=['POST'])
def match_resume():
    user_resume_data = request.form.get("resume")
    print("Resume received")

    raw_output = ai_api.get_booth_recommendations(user_resume_data)
    booth_recomendations = parse_booth_recommendations(raw_output)

    return render_template(
        'match.html',
        resume=user_resume_data,
        booth_recomendations=booth_recomendations,
        no_match_message=NO_MATCH_MESSAGE if not booth_recomendations else None
    )

#method written by AI to make website look better so text isn't just copy pasted onto match screen
def parse_booth_recommendations(raw_output):
    """Parse the numbered company list produced by the AI prompt into a
    list of dicts: [{'company': ..., 'talking_points': ...}, ...]
    Returns an empty list if there are no matches or parsing fails.
    """
    raw_output = raw_output.strip()

    if not raw_output or NO_MATCH_MESSAGE in raw_output:
        return []

    pattern = re.compile(
    r'^\s*\d+\.\s*(?P<company>.+?)\s*\n'
    r'\*\s*Company Breakdown:\s*(?P<breakdown>.+?)\s*\n'
    r'\*\s*Pitch Strategy:\s*(?P<pitch>.+?)'
    r'(?=\n\s*\n\s*\d+\.|\Z)',
    re.DOTALL | re.MULTILINE
)

    results = []
    for match in pattern.finditer(raw_output):
        company = match.group('company').strip()
        breakdown = match.group('breakdown').strip()
        pitch = match.group('pitch').strip()

        results.append({
            "company": company,
            "talking_points": f"{breakdown} | Pitch: {pitch}"
        })

    return results


if __name__ == '__main__':
    app.run(debug=True)