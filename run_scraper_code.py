#run_scraper_code.py

from webscrapeshiftingfingerprint.scrapers import Scrapers

if __name__=="__main__":
    scrapers = Scrapers()
    print("Chrome driver implementation...")
    scrapers.chrome_driver_implementation()
    print("Firefox driver implementation...")
    scrapers.firefox_driver_implementation()
