#run_scraper_code.py

from webscrapeshiftingfingerprint.scrapers import Scrapers

if __name__=="__main__":
    scrapers = Scrapers()

    file = open('URL_values.txt')
    for line in file:
        fields = line.strip().split()
        if fields[0]=="URL":
            print("URL is: ", fields[1])
            scrapers.chrome_driver_implementation_passed_url(fields[1])
            scrapers.firefox_driver_implementation_passed_url(fields[1])
            print("Now with options given...")
            options= scrapers.firefox_options()
            scrapers.firefox_driver_implementation_passed_url_and_options(fields[1], options)
            options= scrapers.chrome_options()
            scrapers.chrome_driver_implementation_passed_url_and_options(fields[1], options)
    #print("Chrome driver implementation...")
    #scrapers.chrome_driver_implementation()
    #print("Firefox driver implementation...")
    #scrapers.firefox_driver_implementation()
