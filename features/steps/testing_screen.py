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

@then('we will log the no screen testing time variance in the saved file')
def we_will_log_the_no_screen_time_variance_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("no screen")

@then('we will log the screen testing time in the saved file')
def we_will_log_the_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("screen")