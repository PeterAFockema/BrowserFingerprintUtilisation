from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('the Firefox screen value has been recorded')
def the_firefox_screen_value_has_been_recorded(context):
    assert test_manager.html_puller_firefox.get_screen_resolution_value() != None

@then('the Firefox screen value is saved')
def the_firefox_screen_value_has_been_recorded(context):
    test_manager.html_puller_firefox.save_screen_resolution_value()
