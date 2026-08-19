from scraper import Scraper
from database_management import DatabaseManager
from app import Flask

db = DatabaseManager("employer.db")


# Commit changes and close the database connection
db.commit_changes()
db.close()

#add_employer(self, name, employment_type, visa_status, majors, degree_level):



        
        
#   Pre push next steps:
#   
#   1. Make a database to store the user interactions so I can count users if the hosting service I use doesn't automatically
#   2. Make sure the data is for the next career fair when UW Madison posts the coming employers
#   3. Advertise


#   Potential future improvements:

#   Add a real test suite (pytest, mocked LLM calls, some integration tests)
#   Dockerize it, add CI (GitHub Actions running tests on every push)
#   Add basic observability — structured logging, maybe a Prometheus/Grafana dashboard tracking request latency and LLM call failures
#   Deploy it somewhere real (Fly.io, Railway, a $5 VPS) so it's a live link, not just a repo
#