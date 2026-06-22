from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('the visitor id for {attributes} is saved')
def step_impl(context, attributes):
    assert test_manager.html_puller_firefox.save_visitor_id_value()