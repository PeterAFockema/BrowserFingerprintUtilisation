from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *

test_manager = TestManager()
screen_increment = 0

'''
The following definitions relate to the Firefox browser.
'''
@given('we declare a Firefox server defined for screen values with no extension')
def we_declare_a_firefox_server_defined_for_screen_values_with_no_extension(context):
    assert test_manager.html_puller_firefox.check_can_pull_HTML_page != False

@when('we view the Firefox page with no screen values interference')
def we_view_the_firefox_page_with_no_screen_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page(), "html.parser").find())
    test_manager.html_puller_firefox= html_puller_firefox
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we have a Firefox page which ran the screen response')
def we_have_a_firefox_page_which_ran_the_screen_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('the Firefox screen value has been recorded')
def the_firefox_screen_value_has_been_recorded(context):
    assert test_manager.html_puller_firefox.get_screen_resolution_value() != None

@then('the Firefox screen value is saved')
def the_firefox_screen_value_has_been_recorded(context):
    test_manager.html_puller_firefox.save_screen_resolution_value()

@then('we will log the time in the saved file')
def we_will_log_the_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file()

@then('the visitor id is saved')
def the_firefox_screen_value_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_screen_resolution_value()

@given('we declare a Firefox server defined for screen values with an extension')
def we_declare_a_firefox_server_defined_for_screen_values_with_an_extension(context):
    assert test_manager.html_puller_firefox.check_can_pull_HTML_page != False

@when('we view the Firefox page with some screen values interference')
def we_view_the_firefox_page_with_some_screen_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension("screen"), "html.parser").find())
    test_manager.html_puller_chrome= html_puller_firefox
    assert test_manager.html_puller_chrome.html_source != "<html></html>" 