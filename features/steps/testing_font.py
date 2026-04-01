from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *

test_manager = TestManager()
font_increment = 0

'''
The following definitions relate to the Firefox browser.
'''
@given('we declare a Firefox server defined for font values with no extension')
def we_declare_a_firefox_server_defined_for_font_values_with_no_extension(context):
    assert test_manager.html_puller_firefox.check_can_pull_HTML_page != False

@when('we view the Firefox page with no font values interference')
def we_view_the_firefox_page_with_no_font_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page(), "html.parser").find())
    test_manager.html_puller_firefox= html_puller_firefox
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we have a Firefox page which ran the font response')
def we_have_a_firefox_page_which_ran_the_font_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('the Firefox font value has been recorded')
def the_firefox_font_value_has_been_recorded(context):
    assert test_manager.html_puller_firefox.get_fonts_value() != None

@then('the Firefox font value is saved')
def the_firefox_font_value_has_been_recorded(context):
    test_manager.html_puller_firefox.save_fonts_value()

@then('we will log the font testing time in the saved file')
def we_will_log_the_font_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("font")

@then('the visitor id for font is saved')
def the_firefox_visitor_id_for_font_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()

@given('we declare a Firefox server defined for font values with an extension')
def we_declare_a_firefox_server_defined_for_font_values_with_an_extension(context):
    assert test_manager.html_puller_firefox.check_can_pull_HTML_page != False

@when('we view the Firefox page with some font values interference')
def we_view_the_firefox_page_with_some_font_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension("font"), "html.parser").find())
    test_manager.html_puller_chrome= html_puller_firefox
    assert test_manager.html_puller_chrome.html_source != "<html></html>" 