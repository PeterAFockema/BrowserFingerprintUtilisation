from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# options = Options()
print("1")
# options.binary_location = '<YOUR LOCATION HERE>'

# Initialize the Firefox driver
driver = webdriver.Firefox()
print("2")
# Navigate to the URL
driver.get('https://google.com')
print("3")
# Print the title page
print(driver.title)
print("4")
# Here we close the browser when done
driver.quit()
print("5")