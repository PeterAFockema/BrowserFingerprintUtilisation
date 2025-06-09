#run_scraper_code.py

from webscrapeshiftingfingerprint.scrapers import Scrapers

if __name__=="__main__":
    scrapers = Scrapers()
    scrapers.chrome_driver_implementation()
