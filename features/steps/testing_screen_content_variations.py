from behave import *
from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('we have a Firefox page which ran the no availHeight or availWidth or colorDepth values interference response')
@then('we have a Firefox page which ran the availHeight response')
@then('we have a Firefox page which ran the availWidth response')
@then('we have a Firefox page which ran the colorDepth response')
@then('we have a Firefox page which ran the devicePixelRatio response')
@then('we have a Firefox page which ran the availHeight and availWidth values response')
@then('we have a Firefox page which ran the availHeight and colorDepth values response')
@then('we have a Firefox page which ran the availHeight and devicePixelRatio values response')
@then('we have a Firefox page which ran the availWidth and colorDepth values response')
@then('we have a Firefox page which ran the availWidth and devicePixelRatio values response')
@then('we have a Firefox page which ran the colorDepth and devicePixelRatio values response')
@then('we have a Firefox page which ran the availHeight and availWidth and colorDepth values response')
@then('we have a Firefox page which ran the availHeight and availWidth and devicePixelRatio values response')
@then('we have a Firefox page which ran the availHeight and devicePixelRatio and colorDepth values response')
@then('we have a Firefox page which ran the availWidth and devicePixelRatio and colorDepth values response')
@then('we have a Firefox page which ran the availHeight and availWidth and devicePixelRatio and colorDepth values response')
def we_have_a_firefox_page_which_ran_the_no_availHeight_or_availWidth_or_colorDepth_values_interference_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we will log the no availHeight or availWidth or colorDepth values interference testing time in the saved file')
def we_will_log_the_no_availHeight_or_availWidth_or_colorDepth_values_interference_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("no availHeight or availWidth or colorDepth values interference")

@then('we will log the availHeight testing time in the saved file')
def we_will_log_the_availHeight_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("availHeight values interference")

@then('we will log the availWidth testing time in the saved file')
def we_will_log_the_availWidth_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("availWidth values interference")

@then('we will log the colorDepth testing time in the saved file')
def we_will_log_the_colorDepth_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("colorDepth values interference")

@then('we will log the devicePixelRatio testing time in the saved file')
def we_will_log_the_devicePixelRatio_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("devicePixelRatio values interference")
    
@then('we will log the availHeight and availWidth values testing time in the saved file')
def we_will_log_the_availHeight_and_availWidth_values_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("availHeight and availWidth values interference")

@then('we will log the availHeight and colorDepth values testing time in the saved file')
def we_will_log_the_availHeight_and_colorDepth_values_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("availHeight and colorDepth values interference")

@then('we will log the availHeight and devicePixelRatio values testing time in the saved file')
def we_will_log_the_availHeight_and_devicePixelRatio_values_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("availHeight and devicePixelRatio values interference")

@then('we will log the availWidth and colorDepth values testing time in the saved file')
def we_will_log_the_availWidth_and_colorDepth_values_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("availWidth and colorDepth values interference")

@then('we will log the availWidth and devicePixelRatio values testing time in the saved file')
def we_will_log_the_availWidth_and_devicePixelRatio_values_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("availWidth and devicePixelRatio values interference")

@then('we will log the colorDepth and devicePixelRatio values testing time in the saved file')
def we_will_log_the_colorDepth_and_devicePixelRatio_values_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("colorDepth and devicePixelRatio values interference")

@then('we will log the availHeight and availWidth and colorDepth values testing time in the saved file')
def we_will_log_the_availHeight_and_availWidth_and_colorDepth_values_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("availHeight and availWidth and colorDepth values interference")

@then('we will log the availHeight and availWidth and devicePixelRatio values testing time in the saved file')
def we_will_log_the_availHeight_and_availWidth_and_devicePixelRatio_values_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("availHeight and availWidth and devicePixelRatio values interference")

@then('we will log the availHeight and devicePixelRatio and colorDepth values testing time in the saved file')
def we_will_log_the_availHeight_and_devicePixelRatio_and_colorDepth_values_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("availHeight and devicePixelRatio and colorDepth values interference")

@then('we will log the availWidth and devicePixelRatio and colorDepth values testing time in the saved file')
def we_will_log_the_availWidth_and_devicePixelRatio_and_colorDepth_values_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("availWidth and devicePixelRatio and colorDepth values interference")

@then('we will log the availHeight and availWidth and devicePixelRatio and colorDepth values testing time in the saved file')
def we_will_log_the_availHeight_and_availWidth_and_devicePixelRatio_and_colorDepth_values_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("availHeight and availWidth and devicePixelRatio and colorDepth values interference")

@then('the visitor id for no availHeight or availWidth or colorDepth values interference is saved')
@then('the visitor id for availHeight value variation is saved')
@then('the visitor id for availWidth value variation is saved')
@then('the visitor id for colorDepth value variation is saved')
@then('the visitor id for devicePixelRatio value variation is saved')
@then('the visitor id for availHeight and availWidth values variation value is saved')
@then('the visitor id for availHeight and colorDepth values variation value is saved')
@then('the visitor id for availHeight and devicePixelRatio values variation value is saved')
@then('the visitor id for availWidth and colorDepth values variation value is saved')
@then('the visitor id for availWidth and devicePixelRatio values variation value is saved')
@then('the visitor id for colorDepth and devicePixelRatio values variation value is saved')
@then('the visitor id for availHeight and availWidth and colorDepth values variation value is saved')
@then('the visitor id for availHeight and availWidth and devicePixelRatio values variation value is saved')
@then('the visitor id for availHeight and devicePixelRatio and colorDepth values variation value is saved')
@then('the visitor id for availWidth and devicePixelRatio and colorDepth values variation value is saved')
@then('the visitor id for availHeight and availWidth and devicePixelRatio and colorDepth values variation value is saved')
def the_visitor_id_for_no_availHeight_or_availWidth_or_colorDepth_values_interference_is_saved(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()