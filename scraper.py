import sqlite3
import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        result = requests.get(self.url)
        return BeautifulSoup(result.text, "html.parser")
    
    def scrape_and_store(self, db_manager):
        doc = self.fetch_data()
        table = doc.find("table")

        if not table:
            print("Could not find a table on the page.")
            return

        rows = table.find_all("tr")
        
        for index, row in enumerate(rows):
            if index == 0:
                continue 
                
            cells = row.find_all(["th", "td"])
            row_data = [cell.text.strip() for cell in cells]
            
            if len(row_data) == 5:
                db_manager.add_employer(row_data[0], row_data[1], row_data[2], row_data[3], row_data[4])
            elif row_data:
                print(f"Skipping malformed row: {row_data}")
                
        db_manager.commit_changes()
        print("Scraping complete. Data saved to employer.db!")