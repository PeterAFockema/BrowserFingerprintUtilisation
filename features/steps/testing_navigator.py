from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('the Firefox navigator value has been recorded')
def the_firefox_navigator_value_has_been_recorded(context):
    assert test_manager.html_puller_firefox.get_web_gl_value() != None

@then('the Firefox navigator value is saved')
def the_firefox_navigator_value_is_saved(context):
    print("TODO: look at how to extract navigator value (if available) from FingerprintJS")
    # assert test_manager.html_puller_firefox.save_navigator_value() #TODO: If this is available from FingerprintJS, record
