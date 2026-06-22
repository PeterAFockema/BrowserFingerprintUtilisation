from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('we have a Firefox page which ran the webRTC response')
def we_have_a_firefox_page_which_ran_the_webRTC_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('the Firefox webRTC value has been recorded')
def the_firefox_webRTC_value_has_been_recorded(context):
    assert test_manager.html_puller_firefox.get_web_gl_value() != None

@then('the Firefox webRTC value is saved')
def the_firefox_webRTC_value_is_saved(context):
    print("TODO: look at how to extract webRTC value (if available) from FingerprintJS")
    # assert test_manager.html_puller_firefox.save_webRTC_value() #TODO: If this is available from FingerprintJS, record

@then('we will log the webRTC testing time in the saved file')
def we_will_log_the_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("webRTC")