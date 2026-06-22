from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''
@given('we declare a Firefox server defined for font values with no extension')
def we_declare_a_firefox_server_defined_for_font_values_with_no_extension(context):
    assert test_manager.html_puller_firefox.check_can_pull_HTML_page != False

@then('we have a Firefox page which ran the font response')
def we_have_a_firefox_page_which_ran_the_font_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('the Firefox font value has been recorded')
def the_firefox_font_value_has_been_recorded(context):
    assert test_manager.html_puller_firefox.get_fonts_value() != None

@then('the Firefox font value is saved')
def the_firefox_font_value_has_been_recorded(context):
    test_manager.html_puller_firefox.save_fonts_value()

@then('we will log the no font testing time in the saved file')
def we_will_log_the_no_font_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("no font")

@then('we will log the font testing time in the saved file')
def we_will_log_the_font_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("font")