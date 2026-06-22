from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('we have a Firefox page which ran the clientRects response')
def we_have_a_firefox_page_which_ran_the_clientRects_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('the Firefox clientRects value has been recorded')
def the_firefox_clientRects_value_has_been_recorded(context):
    assert test_manager.html_puller_firefox.get_web_gl_value() != None

@then('the Firefox clientRects value is saved')
def the_firefox_clientRects_value_has_been_recorded(context):
    print("TODO: look at how to extract clientRects value (if available) from FingerprintJS")
    # assert test_manager.html_puller_firefox.save_clientRects_value() #TODO: If this is available from FingerprintJS, record

@then('we will log the clientRects testing time in the saved file')
def we_will_log_the_clientRects_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects")

@then('the visitor id for clientRects is saved')
def the_firefox_visitor_id_for_clientRects_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()

@when('we view the Firefox page with some clientRects values interference')
def we_view_the_firefox_page_with_some_clientRects_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_string("clientRects"), "html.parser").find())
    test_manager.html_puller_chrome= html_puller_firefox
    assert test_manager.html_puller_chrome.html_source != "<html></html>" 