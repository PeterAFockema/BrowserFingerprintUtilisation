from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *

test_manager = TestManager()
battery_and_havigator_and_screen_and_webgl_increment = 0

'''
The following definitions relate to the Firefox browser.
'''

@when('we view the Firefox page with some battery and havigator and screen and webgl and webRTC values interference')
def we_view_the_firefox_page_with_some_battery_and_havigator_and_screen_and_webRTC_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["battery", "havigator", "screen", "webgl", "webRTC"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@then('we have a Firefox page which ran the battery and havigator and screen and webgl and webgl response')
@then('we have a Firefox page which ran the battery and havigator and screen and webgl and webRTC response')
def we_have_a_firefox_page_which_ran_the_battery_and_havigator_and_screen_and_other_features_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we will log the battery and havigator and screen and webgl and webgl testing time in the saved file')
def we_will_log_the_battery_and_havigator_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and havigator and screen and webgl and webgl")

@then('we will log the battery_and_havigator and webRTC testing time in the saved file')
def we_will_log_the_battery_and_havigator_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and havigator and screen and webgl and webRTC")

@then('the visitor id for battery and havigator and screen and webgl and webRTC is saved')
def the_firefox_visitor_id_for_battery_and_havigator_and_screen_and_webgl_and_other_features_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()
