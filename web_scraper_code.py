from selenium import webdriver

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Navigate to the URL
driver.get('https://google.com')

# Print the title page
print(driver.title)

# Here we close the browser when done
driver.quit()
