from ScrapeHTML.pull_web_html_chrome import *
from ScrapeHTML.pull_web_html_firefox import *

class TestManager():
    'Test Manager class used for testing software'
    
    html_puller_chrome = HTMLPullerUsingChrome()
    html_puller_firefox = HTMLPullerUsingFirefox()

    def __init__(self) -> None:
        pass