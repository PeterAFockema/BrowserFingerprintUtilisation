#scrapers.py

from selenium import webdriver

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
