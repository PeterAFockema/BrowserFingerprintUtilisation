from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
''' 

@then('we will log the battery and audio testing time in the saved file')
def we_will_log_the_battery_and_audio_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and battery")

@then('we will log the battery and canvas testing time in the saved file')
def we_will_log_the_battery_and_canvas_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and canvas")

@then('we will log the battery and clientRects testing time in the saved file')
def we_will_log_the_battery_and_clientRects_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and clientRects")

@then('we will log the battery and font testing time in the saved file')
def we_will_log_the_battery_and_font_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and font")

@then('we will log the battery and navigator testing time in the saved file')
def we_will_log_the_battery_and_navigator_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and navigator")

@then('we will log the battery and screen testing time in the saved file')
def we_will_log_the_battery_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and screen")

@then('we will log the battery and webgl testing time in the saved file')
def we_will_log_the_battery_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and webgl")

@then('we will log the battery and webRTC testing time in the saved file')
def we_will_log_the_battery_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and webRTC")