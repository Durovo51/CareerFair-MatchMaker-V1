from flask import Flask, render_template, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

    
@app.route('/match', methods=['POST'])
def match_resume():
    user_resume_data = request.form.get("resume")
    print("User Resume Data:", user_resume_data)
    return render_template('match.html', resume=user_resume_data)

if __name__ == '__main__':
    app.run(debug=True)
