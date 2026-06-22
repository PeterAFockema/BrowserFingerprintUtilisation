from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('we will log the audio and battery testing time in the saved file')
def we_will_log_the_audio_and_battery_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and battery")

@then('we will log the audio and canvas testing time in the saved file')
def we_will_log_the_audio_and_canvas_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and canvas")

@then('we will log the audio and clientRects testing time in the saved file')
def we_will_log_the_audio_and_clientRects_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and clientRects")

@then('we will log the audio and font testing time in the saved file')
def we_will_log_the_audio_and_font_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and font")

@then('we will log the audio and navigator testing time in the saved file')
def we_will_log_the_audio_and_navigator_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and navigator")

@then('we will log the audio and screen testing time in the saved file')
def we_will_log_the_audio_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and screen")

@then('we will log the audio and webgl testing time in the saved file')
def we_will_log_the_audio_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and webgl")

@then('we will log the audio and webRTC testing time in the saved file')
def we_will_log_the_audio_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and webRTC")
