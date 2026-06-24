import sqlite3
import requests
from bs4 import BeautifulSoup

class DatabaseManager:
    def __init__(self, db_name="employer.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.setup_table()

    def setup_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS employers (
                            company text,
                            employment_type text,
                            sponsors_visas text,
                            majors text,
                            degree_level text
                            )""")
        self.connection.commit()

    def add_employer(self, name, employment_type, visa_status, majors, degree_level):
        self.cursor.execute("INSERT INTO employers VALUES (?, ?, ?, ?, ?)", 
                        (name, employment_type, visa_status, majors, degree_level))
        
    def commit_changes(self):
        self.connection.commit()

    # Fixed: Renamed to match the main block below
    def close(self):
        self.connection.close()