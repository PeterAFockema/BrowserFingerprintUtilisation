from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
''' 

@then('we have a Firefox page which ran the battery and audio response')
@then('we have a Firefox page which ran the battery and canvas response')
@then('we have a Firefox page which ran the battery and clientRects response')
@then('we have a Firefox page which ran the battery and font response')
@then('we have a Firefox page which ran the battery and navigator response')
@then('we have a Firefox page which ran the battery and screen response')
@then('we have a Firefox page which ran the battery and webgl response')
@then('we have a Firefox page which ran the battery and webRTC response')
def we_have_a_firefox_page_which_ran_the_battery_and_other_features_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

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