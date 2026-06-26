from flask import Flask, render_template, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
import ai_api 

app = Flask(__name__)


#Home page
@app.route('/')
def index():
    return render_template("index.html")

#Resume output page
@app.route('/match', methods=['POST'])
def match_resume():
    user_resume_data = request.form.get("resume")
    print("Resume received")

    booth_recommendations = ai_api.get_booth_recommendations(user_resume_data)

    return render_template('match.html', resume=user_resume_data, booth_recomendations=booth_recommendations)


if __name__ == '__main__':
    app.run(debug=True)