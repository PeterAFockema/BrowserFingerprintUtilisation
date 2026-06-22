from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''


@then('we will log the webrtc and battery testing time in the saved file')
def we_will_log_the_webrtc_and_battery_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("webrtc and battery")

@then('we will log the webrtc and audio testing time in the saved file')
def we_will_log_the_webrtc_and_audio_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("webrtc and audio")

@then('we will log the webrtc and canvas testing time in the saved file')
def we_will_log_the_webrtc_and_canvas_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("webrtc and canvas")

@then('we will log the webrtc and clientRect testing time in the saved file')
def we_will_log_the_webrtc_and_clientRect_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("webrtc and clientRect")

@then('we will log the webrtc and font testing time in the saved file')
def we_will_log_the_webrtc_and_font_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("webrtc and font")

@then('we will log the webrtc and navigator testing time in the saved file')
def we_will_log_the_webrtc_and_navigator_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("webrtc and navigator")

@then('we will log the webrtc and screen testing time in the saved file')
def we_will_log_the_webrtc_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("webrtc and screen")

@then('we will log the webrtc and webgl testing time in the saved file')
def we_will_log_the_webrtc_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("webrtc and webgl")