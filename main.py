from scraper import Scraper
from database_management import DatabaseManager

if __name__ == "__main__":
    db = DatabaseManager("employer.db")
    scraper = Scraper("https://cdis.wisc.edu/career/")
    
    try:
        scraper.scrape_and_store(db)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        db.close()