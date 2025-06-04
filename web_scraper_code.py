from selenium import webdriver

# Set the path to the Chromedriver
DRIVER_PATH = '/path/to/chromedriver'

# Initialize the Chrome driver
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

# Navigate to the URL
driver.get('https://google.com')

# Here we close the browser when done
driver.quit()
