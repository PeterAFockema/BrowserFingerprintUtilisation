from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''
@given('we declare a Firefox server defined for font values with no extension')
def we_declare_a_firefox_server_defined_for_font_values_with_no_extension(context):
    assert test_manager.html_puller_firefox.check_can_pull_HTML_page != False

@then('the Firefox font value has been recorded')
def the_firefox_font_value_has_been_recorded(context):
    assert test_manager.html_puller_firefox.get_fonts_value() != None

@then('the Firefox font value is saved')
def the_firefox_font_value_has_been_recorded(context):
    test_manager.html_puller_firefox.save_fonts_value()
