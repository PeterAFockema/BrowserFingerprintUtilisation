from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *

test_manager = TestManager()
webgl_increment = 0

'''
The following definitions relate to the Firefox browser.
'''

@then('we have a Firefox page which ran the no parameter and buffer response')
def we_have_a_firefox_page_which_ran_the_no_parameter_and_buffer_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we have a Firefox page which ran the parameter response')
def we_have_a_firefox_page_which_ran_the_parameter_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we have a Firefox page which ran the buffer response')
def we_have_a_firefox_page_which_ran_the_buffer_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we have a Firefox page which ran the parameter and buffer values response')
def we_have_a_firefox_page_which_ran_the_parameter_and_buffer_values_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we will log the no parameter and buffer testing time in the saved file')
def we_will_log_the_no_parameter_and_buffer_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("no parameter and buffer")

@then('we will log the parameter testing time in the saved file')
def we_will_log_the_parameter_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("parameter")

@then('we will log the buffer testing time in the saved file')
def we_will_log_the_buffer_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("buffer")

@then('we will log the parameter and buffer values testing time in the saved file')
def we_will_log_the_parameter_and_buffer_values_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("parameter and buffer")

@then('the visitor id for no parameter and buffer value variation is saved')
def the_firefox_visitor_id_for_no_parameter_and_buffer_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()

@then('the visitor id for parameter value variation is saved')
def the_firefox_visitor_id_for_parameter_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()

@then('the visitor id for buffer value variation is saved')
def the_firefox_visitor_id_for_buffer_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()

@then('the visitor id for parameter and buffer values variation value is saved')
def the_visitor_id_for_parameter_and_buffer_values_variation_value_is_saved(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()
    
# @when('we view the Firefox page with some parameter values interference')
# def we_view_the_firefox_page_with_some_parameter_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_string("parameter"), "html.parser").find())
#     test_manager.html_puller_chrome= html_puller_firefox
#     assert test_manager.html_puller_chrome.html_source != "<html></html>" 

# @when('we view the Firefox page with some buffer values interference')
# def we_view_the_firefox_page_with_some_buffer_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_string("buffer"), "html.parser").find())
#     test_manager.html_puller_chrome= html_puller_firefox
#     assert test_manager.html_puller_chrome.html_source != "<html></html>" 

# @when('we view the Firefox page with parameter and buffer values interference')
# def we_view_the_firefox_page_with_some_webgl_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["parameter", "buffer"]), "html.parser").find())
#     test_manager.html_puller_chrome= html_puller_firefox
#     assert test_manager.html_puller_chrome.html_source != "<html></html>" 