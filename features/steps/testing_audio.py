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

@when('we view the Firefox page with some audio values interference')
def we_view_the_firefox_page_with_some_audio_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_string("audio"), "html.parser").find())
    test_manager.html_puller_chrome= html_puller_firefox
    assert test_manager.html_puller_chrome.html_source != "<html></html>" 