from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *

test_manager = TestManager()
webgl_increment = 0

'''
The following definitions relate to the Firefox browser.
'''

@when('we view the Firefox page with no toBlob and toDataURL values interference')
def we_view_the_firefox_page_with_no_toBlob_and_toDataURL_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page(), "html.parser").find())
    test_manager.html_puller_firefox= html_puller_firefox
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we have a Firefox page which ran the no toBlob and toDataURL response')
def we_have_a_firefox_page_which_ran_the_no_toBlob_and_toDataURL_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we have a Firefox page which ran the toBlob response')
def we_have_a_firefox_page_which_ran_the_toBlob_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we have a Firefox page which ran the toDataURL response')
def we_have_a_firefox_page_which_ran_the_toDataURL_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we have a Firefox page which ran the toBlob and toDataURL values response')
def we_have_a_firefox_page_which_ran_the_toBlob_and_toDataURL_values_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we will log the no toBlob and toDataURL testing time in the saved file')
def we_will_log_the_no_toBlob_and_toDataURL_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("no toBlob and toDataURL")

@then('we will log the toBlob testing time in the saved file')
def we_will_log_the_toBlob_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("toBlob")

@then('we will log the toDataURL testing time in the saved file')
def we_will_log_the_toDataURL_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("toDataURL")

@then('we will log the toBlob and toDataURL testing time in the saved file')
def we_will_log_the_toBlob_and_toDataURL_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("toBlob and toDataURL")

@then('the visitor id for no toBlob and toDataURL value variation is saved')
def the_firefox_visitor_id_for_no_toBlob_and_toDataURL_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()

@then('the visitor id for toBlob value variation is saved')
def the_firefox_visitor_id_for_toBlob_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()

@then('the visitor id for toDataURL value variation is saved')
def the_firefox_visitor_id_for_toDataURL_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()

@then('the visitor id for toBlob and toDataURL values variation is saved')
def the_firefox_visitor_id_for_webgl_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()

@when('we view the Firefox page with some toBlob values interference')
def we_view_the_firefox_page_with_some_toBlob_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension("toBlob"), "html.parser").find())
    test_manager.html_puller_chrome= html_puller_firefox
    assert test_manager.html_puller_chrome.html_source != "<html></html>" 

@when('we view the Firefox page with some toDataURL values interference')
def we_view_the_firefox_page_with_some_toDataURL_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension("toDataURL"), "html.parser").find())
    test_manager.html_puller_chrome= html_puller_firefox
    assert test_manager.html_puller_chrome.html_source != "<html></html>" 

@when('we view the Firefox page with toBlob and toDataURL values interference')
def we_view_the_firefox_page_with_some_webgl_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["toBlob", "toDataURL"]), "html.parser").find())
    test_manager.html_puller_chrome= html_puller_firefox
    assert test_manager.html_puller_chrome.html_source != "<html></html>" 