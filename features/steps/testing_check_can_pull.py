from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@given('we declare a Firefox server defined for font values with no extension')
@given('we can pull a page on Firefox')
def we_can_pull_a_page_on_firefox(context):
    assert test_manager.html_puller_firefox.check_can_pull_HTML_page != False