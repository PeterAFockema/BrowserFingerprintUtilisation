#run_scraper_code.py

from webscrapeshiftingfingerprint.scrapers import Scrapers

if __name__=="__main__":
    scrapers = Scrapers()

    file = open('URL_values.txt')
    for line in file:
        fields = line.strip().split()
        if fields[0]=="URL":
            # print("URL is: ", fields[1])
            # scrapers.chrome_driver_implementation_passed_url(fields[1])
            # scrapers.firefox_driver_implementation_passed_url(fields[1])
            # print("Now with options given...")
            # options= scrapers.firefox_options()
            # scrapers.firefox_driver_implementation_passed_url_and_options(fields[1], options)
            # options= scrapers.chrome_options()
            # scrapers.chrome_driver_implementation_passed_url_and_options(fields[1], options)
            print("Now Chrome with mobile parameters...")
            scrapers.chrome_driver_implementation_passed_url_mobile(fields[1])
            # print("Now Firefox with mobile parameters...")
            # scrapers.firefox_driver_implementation_passed_url_mobile(fields[1])
            # print("Now Chrome with tablet parameters...")
            # scrapers.chrome_driver_implementation_passed_url_tablet(fields[1])
            # print("Now Firefox with tablet parameters...")
            # scrapers.firefox_driver_implementation_passed_url_tablet(fields[1])
            # print("Now Chrome with desktop parameters...")
            # scrapers.chrome_driver_implementation_passed_url_desktop(fields[1])
            # print("Now Firefox with desktop parameters...")
            # scrapers.firefox_driver_implementation_passed_url_desktop(fields[1])
            