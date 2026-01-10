# BrowserFingerprintUtilisation

## Notes
We are using Selenium for our Chrome driver, where for
selenium version > 4.12.0 we do not need to download the
Chrome driver manually.
Selenium's in-built tool _Selenium Manager_ automatically
downloads and manages the drivers.

See: 
+ https://www.selenium.dev/documentation/selenium_manager/ 
+ https://www.selenium.dev/blog/2023/status_of_selenium_manager_in_october_2023/

## Use
For testing against a local-machine-hosted browser fingerprinting website, in the WebsiteSetUp folder run:
```
docker build -t basic-website:latest .
docker run -d -p 8080:80 basic-website:latest
```

(Values can be reset in the test.env file)

To test the code, once the environment has been set up, in the current directory run:
```
behave
```

# Developer Notes
Due to the Chrome team removing
```
--load-extension
```
switch on Chrome builds, (see https://github.com/SeleniumHQ/selenium/issues/15788 ), we will
be pivoting to focusing on using other drivers until further notice.
