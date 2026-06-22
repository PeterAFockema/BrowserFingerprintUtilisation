from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('we will log the battery and navigator and screen testing time in the saved file')
def we_will_log_the_battery_and_navigator_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and navigator and screen")

@then('we will log the battery and navigator and webgl testing time in the saved file')
def we_will_log_the_battery_and_navigator_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and navigator and webgl")

@then('we will log the battery and navigator and webRTC testing time in the saved file')
def we_will_log_the_battery_and_navigator_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and navigator and webRTC")
