from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Chrome browser.
'''

@when('we view the Chrome page with no canvas values interference')
def we_view_the_chrome_page_with_no_canvas_values_interference(context):
    html_puller_chrome = test_manager.html_puller_chrome
    bool(BeautifulSoup(html_puller_chrome.pull_HTML_page(), "html.parser").find())
    test_manager.html_puller_chrome= html_puller_chrome
    assert test_manager.html_puller_chrome.html_source != "<html></html>"

@then('we have a Chrome page which ran the canvas response')
def we_have_a_chrome_page_which_ran_the_canvas_response(context):
    assert test_manager.html_puller_chrome.html_source != "<html></html>"

@then('the Chrome canvas value has been recorded')
def the_chrome_canvas_value_has_been_recorded(context):
    assert test_manager.html_puller_chrome.get_canvas_value() != None

@then('the Firefox canvas value is saved')
def the_firefox_canvas_value_has_been_recorded(context):
    test_manager.html_puller_firefox.save_canvas_value()

@then('we will log the canvas testing time in the saved file')
def we_will_log_the_canvas_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas")

@given('we declare a Chrome server defined for canvas values with an extension')
def we_declare_a_chrome_server_defined_for_canvas_values_with_an_extension(context):
    assert test_manager.html_puller_chrome.check_can_pull_HTML_page != False

@when('we view the Chrome page with some canvas values interference')
def we_view_the_chrome_page_with_some_canvas_values_interference(context):
    html_puller_chrome = test_manager.html_puller_chrome
    bool(BeautifulSoup(html_puller_chrome.pull_HTML_page_with_canvas_extension(), "html.parser").find())
    test_manager.html_puller_chrome= html_puller_chrome
    assert test_manager.html_puller_chrome.html_source != "<html></html>" 

'''
The following definitions relate to the Firefox browser.
'''

@given('we can pull a page on Firefox')
def we_can_pull_a_page_on_firefox(context):
    assert test_manager.html_puller_firefox.check_can_pull_HTML_page != False

@then('we have a Firefox page which ran the canvas response')
def we_have_a_firefox_page_which_ran_the_canvas_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('the Firefox canvas value has been recorded')
def the_firefox_canvas_value_has_been_recorded(context):
    assert test_manager.html_puller_firefox.get_canvas_value() != None

@when('we view the Firefox page with some canvas values interference')
def we_view_the_firefox_page_with_some_canvas_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_canvas_extension(), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 