import configparser
from bs4 import BeautifulSoup
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
#Import the server code
from ScrapeHTML.server_usage import *
#Import the display code
from ScrapeHTML.display import *
#Import the scrapers code
from shiftingbrowserfingerprints.scrapers_objects import Scrapers

# from firefox_scrapers_objects import Scrapers_Firefox

class HTMLPullerUsingFirefox():
    'Base code for HTML Pulling'
  
    #Server
    server = ServerUsage()
    #Display
    display_class = Display()

    #The HTML source element initlalised to empty HTML string
    html_source = "<html></html>"

    #Has the audio Promise been inserted?
    audio_promise_insert_status = False

    def __init__(self) -> None:
        pass

    #Update our recorder HTML values with those from the page source
    @classmethod
    def updateHTML(HTMLPullerClass, new_html_source):
        HTMLPullerClass.html_source = new_html_source

    def get_fingerprinting_url_server_host(self):
        config = configparser.ConfigParser()
        config.read('test.env')
        string_to_return = str(config.get('FINGERPRINT_SERVER', 'FINGERPRINT_SERVER_HOST'))
        print("The fingerprint server is: ", string_to_return)
        return string_to_return
    
    def get_fingerprinting_url_server_host(self):
        config = configparser.ConfigParser()
        config.read('test.env')
        string_to_return = str(config.get('FINGERPRINT_SERVER', 'FINGERPRINT_SERVER_HOST'))
        print("The fingerprint server is: ", string_to_return)
        return string_to_return

    def navigateToFingerprintPage(self, driver):
        # Go to Fingerprinting page
        url = self.get_fingerprinting_url_server_host()
        driver.get(url)
        return driver
    
    def resetDefaultValues(self):
        print("resetDefaultValues")
        self.audio_promise_insert_status = False
    
    #0 Combinations
    def check_can_pull_HTML_page(self):
        #Reset our custom default values
        self.resetDefaultValues()
        #Set the Web Driver options
        options = Options()
        # Use headless mode
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-dev-shm-usage')
        print("Building a Firefox driver...")
        scrapers = Scrapers()
        driver = scrapers.firefox_driver_implementation()        # Define the Firefox driver
        #Set the Display Port variable
        self.display_class.setDisplayPortAsEnvironmentVariable()
        #Start the Xvfb server
        server_process = self.server.startTheXvfbServerProcess(self.display_class.display_process)
        #Navigate to Fingerprinting page
        driver = self.navigateToFingerprintPage(driver)
        #Update our recorder HTML values with those from the page source
        self.updateHTML(driver.page_source)
        # Close the browser
        driver.quit()
        #Kill the server
        self.server.killTheXcfbServerProcess(server_process)
        return True

    #1 Combination
    def check_can_pull_HTML_page_with_canvas_extension_added(self):
        #Reset our custom default values
        self.resetDefaultValues()
        # options = Options()
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-dev-shm-usage')
        # options.add_extension('TODO: add extension here') #TODO: Add Extension here
        print("Building a Firefox driver...")
        scrapers = Scrapers()
        driver = scrapers.firefox_driver_implementation() #will need to add extension
        #Set the Display Port variable
        self.display_class.setDisplayPortAsEnvironmentVariable()
        #Start the Xvfb server
        server_process = self.server.startTheXvfbServerProcess(self.display_class.display_process)
        print("Performing a driver.get() on fingerprinting page...")
        #Navigate to Fingerprinting page
        url = self.get_fingerprinting_url_server_host()
        driver.get(url)
        print(driver.title)
        #Update our recorder HTML values with those from the page source
        self.updateHTML(driver.page_source)
        print("Closing the Firefox driver down...")
        driver.close()
        #Kill the server
        self.server.killTheXcfbServerProcess(server_process)
        return True

    ###################################################
    ###PULLING HTML CODE###############################
    ###################################################
    #0 Combinations
    def pull_HTML_page(self):
        #Reset our custom default values
        self.resetDefaultValues()
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        print("Building a Firefox driver...")
        # Initialize the Firefox driver
        driver = webdriver.Firefox()
        url = self.get_fingerprinting_url_server_host()
        print("Performing a driver.get() on fingerprinting page...")
        driver.get(url) # Navigate to the URL
        #'Render' the Fingerprinting page with the Promise executed
        driver = self.renderTheFingerprintPageValues(driver)
        #Update our recorder HTML values with those from the page source
        self.updateHTML(driver.page_source)
        #Set the Display Port variable
        self.display_class.setDisplayPortAsEnvironmentVariable()
        #Update our recorder HTML values with those from the page source
        self.updateHTML(driver.page_source)
        print(driver.title)
        print("Closing the Firefox driver down...")
        driver.close()
        return self.html_source
    
    #1 Combinations

    def pull_HTML_page_with_canvas_extension(self):
        #Reset our custom default values
        self.resetDefaultValues()
        print("Building a Firefox driver...")
        scrapers = Scrapers()
        driver = scrapers.firefox_driver_implementation() #TODO: Need to add canvas extension
        #Navigate to Fingerprinting page
        url = self.get_fingerprinting_url_server_host()
        print("Performing a driver.get() on fingerprinting page...")
        driver.get(url)
        #'Render' the Fingerprinting page with the Promise executed
        driver = self.renderTheFingerprintPageValues(driver)
        #Update our recorder HTML values with those from the page source
        self.updateHTML(driver.page_source)
        #Set the Display Port variable
        self.display_class.setDisplayPortAsEnvironmentVariable()
        #Update our recorder HTML values with those from the page source
        self.updateHTML(driver.page_source)
        print("Closing the Firefox driver down...")
        driver.close()
        #Kill the server
        return self.html_source

    '''
    We are overloading the pull_HTML_page_with_extension() to
    handle multiple passed parameters.
    '''
    def pull_HTML_page_with_extension(self, passed_value: str):
        print("LOOK HERE: DEBUG: pull_HTML_page_with_extension passed_value: ", passed_value)
        #Reset our custom default values
        self.resetDefaultValues()
        print("Building a Firefox driver...")
        scrapers = Scrapers()
        driver = scrapers.firefox_driver_extension_implementation(passed_value)
        #Navigate to Fingerprinting page
        url = self.get_fingerprinting_url_server_host()
        print("Performing a driver.get() on fingerprinting page...")
        driver.get(url)
        #'Render' the Fingerprinting page with the Promise executed
        driver = self.renderTheFingerprintPageValues(driver)
        #Update our recorder HTML values with those from the page source
        self.updateHTML(driver.page_source)
        #Set the Display Port variable
        self.display_class.setDisplayPortAsEnvironmentVariable()
        #Update our recorder HTML values with those from the page source
        self.updateHTML(driver.page_source)
        print("Closing the Firefox driver down...")
        driver.close()
        #Kill the server
        return self.html_source

    # 'Render' the Fingerprinting page
    def renderTheFingerprintPageValues(self, driver):
        try:
            print("In the rendering part!")
            #waiting for Fingerprinting data to be visible
            delay=20 #20 second delay
            print("About to delay...")
            WebDriverWait(driver, delay).until(EC.visibility_of_element_located((By.CLASS_NAME, 'visitorIdIdentifier')))
            print("Delay finished...")
            print(len(driver.page_source))
        #raises Exception if element is not visible within delay duration
        except TimeoutException:
            print("Timeout!!!")
        return driver
    
    def getAudioUpdateStatus(self):
        return self.audio_promise_insert_status
    
    def get_driver_options(self):
        options = Options()
        # Use headless mode
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        return options
    
    # Savers
    def log_time_in_save_file(self, passed_value:str):
        value_to_write = datetime.datetime.now()
        with open('logfile.txt', 'w') as file:
            file.write(passed_value+ " Date&Time, "+ value_to_write)
        return True
    
    def save_audio_value(self):
        soup = BeautifulSoup(self.html_source, "html.parser")
        print("The html content is now: ", self.html_source)
        for child in soup.descendants:
            if child.name:
                print(child.name)
        print("p: ", soup.find('p', attrs={'id':'audioIdentifier'}))
        value_to_write = soup.find('p', attrs={'id':'audioIdentifier'})
        with open('logfile.txt', 'w') as file:
            file.write("screen_resolution, "+ value_to_write)
        return True
    
    def save_fonts_value(self):
        soup = BeautifulSoup(self.html_source, "html.parser")
        print("The html content is now: ", self.html_source)
        for child in soup.descendants:
            if child.name:
                print(child.name)
        print("p: ", soup.find('p', attrs={'id':'fontsIdentifier'}))
        value_to_write = soup.find('p', attrs={'id':'fontsIdentifier'})
        with open('logfile.txt', 'w') as file:
            file.write("screen_resolution, "+ value_to_write)
        return True

    def save_screen_resolution_value(self):
        soup = BeautifulSoup(self.html_source, "html.parser")
        print("The html content is now: ", self.html_source)
        for child in soup.descendants:
            if child.name:
                print(child.name)
        print("p: ", soup.find('p', attrs={'id':'screenResolutionIdentifier'}))
        value_to_write = soup.find('p', attrs={'id':'screenResolutionIdentifier'}).get_text()
        with open('logfile.txt', 'w') as file:
            file.write("screen_resolution, "+ value_to_write)
        return True

    def save_web_gl_value(self):
        soup = BeautifulSoup(self.html_source, "html.parser")
        print("The html content is now: ", self.html_source)
        for child in soup.descendants:
            if child.name:
                print(child.name)
        print("p: ", soup.find('p', attrs={'id':'webGLBasicsIdentifier'}))
        value_to_write = soup.find('p', attrs={'id':'webGLBasicsIdentifier'})
        with open('logfile.txt', 'w') as file:
            file.write("screen_resolution, "+ value_to_write)
        return True

    def save_plugins_value(self):
        soup = BeautifulSoup(self.html_source, "html.parser")
        print("The html content is now: ", self.html_source)
        for child in soup.descendants:
            if child.name:
                print(child.name)
        print("p: ", soup.find('p', attrs={'id':'pluginsIdentifier'}))
        value_to_write = soup.find('p', attrs={'id':'pluginsIdentifier'})
        with open('logfile.txt', 'w') as file:
            file.write("screen_resolution, "+ value_to_write)
        return True
    
    def save_canvas_value(self):
        soup = BeautifulSoup(self.html_source, "html.parser")
        print("The html content is now: ", self.html_source)
        for child in soup.descendants:
            if child.name:
                print(child.name)
        print("div: ", soup.find('div', attrs={'id':'canvasIdentifier'}))
        value_to_write = soup.find('div', attrs={'id':'canvasIdentifier'})
        with open('logfile.txt', 'w') as file:
            file.write("screen_resolution, "+ value_to_write)
        return True
    
    def save_visitor_id_value(self):
        soup = BeautifulSoup(self.html_source, "html.parser")
        print("The html content is now: ", self.html_source)
        for child in soup.descendants:
            if child.name:
                print(child.name)
        print("p: ", soup.find('p', attrs={'id':'visitorIdIdentifier'}))
        value_to_write = soup.find('p', attrs={'id':'visitorIdIdentifier'})
        with open('logfile.txt', 'w') as file:
            file.write("screen_resolution, "+ value_to_write)
        return True
    
    # Getters
    def getAudioUpdateStatus(self):
        return self.audio_promise_insert_status
    
    def get_driver_options(self):
        options = Options()
        # Use headless mode
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        return options
    
    def get_audio_value(self):
        soup = BeautifulSoup(self.html_source, "html.parser")
        print("The html content is now: ", self.html_source)
        for child in soup.descendants:
            if child.name:
                print(child.name)
        print("p: ", soup.find('p', attrs={'id':'audioIdentifier'}))
        return soup.find('p', attrs={'id':'audioIdentifier'})

    def get_fonts_value(self):
        soup = BeautifulSoup(self.html_source, "html.parser")
        print("The html content is now: ", self.html_source)
        for child in soup.descendants:
            if child.name:
                print(child.name)
        print("p: ", soup.find('p', attrs={'id':'fontsIdentifier'}))
        return soup.find('p', attrs={'id':'fontsIdentifier'})

    def get_screen_resolution_value(self):
        soup = BeautifulSoup(self.html_source, "html.parser")
        print("The html content is now: ", self.html_source)
        for child in soup.descendants:
            if child.name:
                print(child.name)
        print("p: ", soup.find('p', attrs={'id':'screenResolutionIdentifier'}))
        return soup.find('p', attrs={'id':'screenResolutionIdentifier'})

    def get_web_gl_value(self):
        soup = BeautifulSoup(self.html_source, "html.parser")
        print("The html content is now: ", self.html_source)
        for child in soup.descendants:
            if child.name:
                print(child.name)
        print("p: ", soup.find('p', attrs={'id':'webGLBasicsIdentifier'}))
        return soup.find('p', attrs={'id':'webGLBasicsIdentifier'})

    def get_plugins_value(self):
        soup = BeautifulSoup(self.html_source, "html.parser")
        print("The html content is now: ", self.html_source)
        for child in soup.descendants:
            if child.name:
                print(child.name)
        print("p: ", soup.find('p', attrs={'id':'pluginsIdentifier'}))
        return soup.find('p', attrs={'id':'pluginsIdentifier'})
    
    def get_canvas_value(self):
        soup = BeautifulSoup(self.html_source, "html.parser")
        print("The html content is now: ", self.html_source)
        for child in soup.descendants:
            if child.name:
                print(child.name)
        print("div: ", soup.find('div', attrs={'id':'canvasIdentifier'}))
        return soup.find('div', attrs={'id':'canvasIdentifier'})

    def get_visitor_id_value(self):
        soup = BeautifulSoup(self.html_source, "html.parser")
        print("The html content is now: ", self.html_source)
        for child in soup.descendants:
            if child.name:
                print(child.name)
        print("p: ", soup.find('p', attrs={'id':'visitorIdIdentifier'}))
        return soup.find('p', attrs={'id':'visitorIdIdentifier'})
    
    #Setters
    def setDefaultValues(self, audioStatus):
        print("setDefaultValues")
        self.audio_promise_insert_status = audioStatus