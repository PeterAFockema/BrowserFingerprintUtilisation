from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('we will log the no toBlob and toDataURL testing time in the saved file')
def we_will_log_the_no_toBlob_and_toDataURL_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("no toBlob and toDataURL")

@then('we will log the toBlob testing time in the saved file')
def we_will_log_the_toBlob_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("toBlob")

@then('we will log the toDataURL testing time in the saved file')
def we_will_log_the_toDataURL_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("toDataURL")

@then('we will log the toBlob and toDataURL values testing time in the saved file')
def we_will_log_the_toBlob_and_toDataURL_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("toBlob and toDataURL")

@when('we view the Firefox page with some toBlob values interference')
def we_view_the_firefox_page_with_some_toBlob_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_string("toBlob"), "html.parser").find())
    test_manager.html_puller_chrome= html_puller_firefox
    assert test_manager.html_puller_chrome.html_source != "<html></html>" 
