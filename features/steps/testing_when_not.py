from behave import *
from bs4 import BeautifulSoup

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@when('we view the Firefox page with no {interference_type} values interference')
@when('we view the Firefox page with no {interference_type} interference')
def step_impl(context, interference_type):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page(), "html.parser").find())
    test_manager.html_puller_firefox = html_puller_firefox
    assert test_manager.html_puller_firefox.html_source != "<html></html>"