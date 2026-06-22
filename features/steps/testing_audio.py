from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('the Firefox audio value has been recorded')
def the_firefox_audio_value_has_been_recorded(context):
    assert test_manager.html_puller_firefox.get_web_gl_value() != None

@then('the Firefox audio value is saved')
def the_firefox_audio_value_has_been_recorded(context):
    test_manager.html_puller_firefox.save_web_gl_value()

@then('we will log the audio testing time in the saved file')
def we_will_log_the_audio_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio")

@when('we view the Firefox page with some audio values interference')
def we_view_the_firefox_page_with_some_audio_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_string("audio"), "html.parser").find())
    test_manager.html_puller_chrome= html_puller_firefox
    assert test_manager.html_puller_chrome.html_source != "<html></html>" 