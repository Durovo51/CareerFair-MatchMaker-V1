import sqlite3
import requests
from bs4 import BeautifulSoup

class DatabaseManager:
    def __init__(self, db_name="employer.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.setup_table()

    def setup_table(self):
        if self is not None:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS employers (
                                company text UNIQUE,
                                employment_type text,
                                sponsors_visas text,
                                majors text,
                                degree_level text
                                )""")
            

    def add_employer(self, name, employment_type, visa_status, majors, degree_level):
        self.cursor.execute("INSERT INTO employers VALUES (?, ?, ?, ?, ?)", 
                        (name, employment_type, visa_status, majors, degree_level))
        
    def commit_changes(self):
        self.connection.commit()

    def clear_old_data(self):
        self.cursor.execute("DELETE FROM employers")
        self.connection.commit()
        print("Data cleared from the employers table.")
    
    def close(self):
        self.connection.close()
        
    def store_all_data_as_string(self):
        self.cursor.execute("SELECT * FROM employers")
        rows = self.cursor.fetchall()
        company_data = ""
        for row in rows:
            company_data += f"Company: {row[0]}, Employment Type: {row[1]}, Sponsors Visas: {row[2]}, Majors: {row[3]}, Degree Level: {row[4]}\n"
        return company_data