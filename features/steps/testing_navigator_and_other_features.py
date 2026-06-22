from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('we will log the navigator and battery testing time in the saved file')
def we_will_log_the_navigator_and_battery_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("navigator and battery")

@then('we will log the navigator and audio testing time in the saved file')
def we_will_log_the_navigator_and_audio_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("navigator and audio")

@then('we will log the navigator and canvas testing time in the saved file')
def we_will_log_the_navigator_and_canvas_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("navigator and canvas")

@then('we will log the navigator and clientRect testing time in the saved file')
def we_will_log_the_navigator_and_clientRect_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("navigator and clientRect")

@then('we will log the navigator and font testing time in the saved file')
def we_will_log_the_navigator_and_font_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("navigator and font")

@then('we will log the navigator and screen testing time in the saved file')
def we_will_log_the_navigator_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("navigator and screen")

@then('we will log the navigator and webgl testing time in the saved file')
def we_will_log_the_navigator_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("navigator and webgl")

@then('we will log the navigator and webRTC testing time in the saved file')
def we_will_log_the_navigator_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("navigator and webRTC")