from behave import *
from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('we have a Firefox page which ran the screen response')
def we_have_a_firefox_page_which_ran_the_screen_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

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

@then('the visitor id for screen value is saved')
def the_firefox_visitor_id_screen_value_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()

# @when('we view the Firefox page with some screen values interference')
# def we_view_the_firefox_page_with_some_screen_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_string("screen"), "html.parser").find())
#     test_manager.html_puller_chrome= html_puller_firefox
#     assert test_manager.html_puller_chrome.html_source != "<html></html>" 