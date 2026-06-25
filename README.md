# Career Fair Matchmaker

A web application designed to optimize the career fair experience. By analyzing a student's resume and relevant background information, the matchmaker identifies and recommends the best booths to visit, maximizing their chances of landing an interview.

## 💻 Tech Stack

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) ![OpenAI](https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white) 

**Backend & Framework**
* **Python:** Handles the core application logic and data processing.
* **Flask:** Lightweight web framework used for RESTful routing and serving the application.

**AI & External Integrations**
* **LLM (Evaluating OpenAI GPT):** Will power the core analysis engine to cross-reference student resumes with company requirements and determine relevancy.

**Data & Architecture**
* **SQLite:** Relational database for storing structured data and efficiently feeding context to the LLM.
* **Beautiful Soup:** Web scraping library utilized to collect, parse, and structure relevant information on companies attending the fair.
