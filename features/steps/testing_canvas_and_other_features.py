from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('we will log the canvas and battery testing time in the saved file')
def we_will_log_the_canvas_and_battery_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and battery")

@then('we will log the canvas and audio testing time in the saved file')
def we_will_log_the_canvas_and_audio_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and audio")

@then('we will log the canvas and clientRects testing time in the saved file')
def we_will_log_the_canvas_and_clientRects_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and clientRects")

@then('we will log the canvas and font testing time in the saved file')
def we_will_log_the_canvas_and_font_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and font")

@then('we will log the canvas and navigator testing time in the saved file')
def we_will_log_the_canvas_and_navigator_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and navigator")

@then('we will log the canvas and screen testing time in the saved file')
def we_will_log_the_canvas_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and screen")

@then('we will log the canvas and webgl testing time in the saved file')
def we_will_log_the_canvas_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and webgl")

@then('we will log the canvas and webRTC testing time in the saved file')
def we_will_log_the_canvas_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and webRTC")