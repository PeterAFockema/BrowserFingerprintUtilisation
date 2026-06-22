from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('we will log the audio and battery and clientRects and font testing time in the saved file')
def we_will_log_the_audio_and_battery_and_clientRects_and_font_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and battery and clientRects and font")

@then('we will log the audio and battery and clientRects and navigator testing time in the saved file')
def we_will_log_the_audio_and_battery_and_clientRects_and_navigator_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and battery and clientRects and navigator")

@then('we will log the audio and battery and clientRects and screen testing time in the saved file')
def we_will_log_the_audio_and_battery_and_clientRects_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and battery and clientRects and screen")

@then('we will log the audio and battery and clientRects and webgl testing time in the saved file')
def we_will_log_the_audio_and_battery_and_clientRects_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and battery and clientRects and webgl")

@then('we will log the audio and battery and clientRects and webRTC testing time in the saved file')
def we_will_log_the_audio_and_battery_and_clientRects_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and battery and clientRects and webRTC")
