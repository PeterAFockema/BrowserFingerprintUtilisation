#scrapers.py

from selenium import webdriver
#from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.firefox.service import Service

class Scrapers(object):
    '''
    A class for web scrapers.
    '''

    def __init__(self):
        print("The Scrapers class initialised...")

    def chrome_driver_implementation(self):
        # Initialize the Chrome driver
        driver = webdriver.Chrome()

        # Navigate to the URL
        driver.get('https://google.com')

        # Print the title page
        print(driver.title)

        # Here we close the browser when done
        driver.quit()

    def firefox_driver_implementation(self):
        #Initialise the Firefox driver
        driver = webdriver.Firefox()

        #Navigate to the URL
        driver.get('https://google.com')

        #Print the title page
        print(driver.title)

        #Here we close the browser when done
        driver.quit()


    def chrome_driver_implementation_passed_url(self, passed_url):
        # Initialize the Chrome driver
        driver = webdriver.Chrome()

        # Navigate to the URL
        driver.get(passed_url)

        # Print the title page
        print(driver.title)

        # Here we close the browser when done
        driver.quit()

    def firefox_driver_implementation_passed_url(self, passed_url):
        #Initialise the Firefox driver
        driver = webdriver.Firefox()

        #Navigate to the URL
        driver.get(passed_url)

        #Print the title page
        print(driver.title)

        #Here we close the browser when done
        driver.quit()
