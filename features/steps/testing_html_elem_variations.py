from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('we have a Firefox page which ran the no offsetHeight and offsetWidth response')
def we_have_a_firefox_page_which_ran_the_no_offsetHeight_and_offsetWidth_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we have a Firefox page which ran the offsetHeight response')
def we_have_a_firefox_page_which_ran_the_offsetHeight_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we have a Firefox page which ran the offsetWidth response')
def we_have_a_firefox_page_which_ran_the_offsetWidth_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we have a Firefox page which ran the offsetHeight and offsetWidth values response')
def we_have_a_firefox_page_which_ran_the_offsetHeight_and_offsetWidth_values_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we will log the no offsetHeight and offsetWidth testing time in the saved file')
def we_will_log_the_no_offsetHeight_and_offsetWidth_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("no offsetHeight and offsetWidth")

@then('we will log the offsetHeight testing time in the saved file')
def we_will_log_the_offsetHeight_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("offsetHeight")

@then('we will log the offsetWidth testing time in the saved file')
def we_will_log_the_offsetWidth_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("offsetWidth")

@then('we will log the offsetHeight and offsetWidth testing time in the saved file')
def we_will_log_the_offsetHeight_and_offsetWidth_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("offsetHeight and offsetWidth")