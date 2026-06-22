from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('we will log the font and battery testing time in the saved file')
def we_will_log_the_font_and_battery_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("font and battery")

@then('we will log the font and audio testing time in the saved file')
def we_will_log_the_font_and_audio_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("font and audio")

@then('we will log the font and canvas testing time in the saved file')
def we_will_log_the_font_and_canvas_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("font and canvas")

@then('we will log the font and clientRect testing time in the saved file')
def we_will_log_the_font_and_clientRect_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("font and clientRect")

@then('we will log the font and navigator testing time in the saved file')
def we_will_log_the_font_and_navigator_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("font and navigator")

@then('we will log the font and screen testing time in the saved file')
def we_will_log_the_font_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("font and screen")

@then('we will log the font and webgl testing time in the saved file')
def we_will_log_the_font_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("font and webgl")

@then('we will log the font and webRTC testing time in the saved file')
def we_will_log_the_font_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("font and webRTC")