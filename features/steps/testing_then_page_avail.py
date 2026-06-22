from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('we have a Firefox page which ran the {components} response')
def step_impl(context, components):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"