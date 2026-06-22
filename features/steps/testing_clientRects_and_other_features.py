from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('we have a Firefox page which ran the clientRects and battery response')
@then('we have a Firefox page which ran the clientRects and audio response')
@then('we have a Firefox page which ran the clientRects and canvas response')
@then('we have a Firefox page which ran the clientRects and font response')
@then('we have a Firefox page which ran the clientRects and navigator response')
@then('we have a Firefox page which ran the clientRects and screen response')
@then('we have a Firefox page which ran the clientRects and webgl response')
@then('we have a Firefox page which ran the clientRects and webRTC response')
def we_have_a_firefox_page_which_ran_the_clientRects_and_other_features_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we will log the clientRects and battery testing time in the saved file')
def we_will_log_the_clientRects_and_battery_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and battery")

@then('we will log the clientRects and audio testing time in the saved file')
def we_will_log_the_clientRects_and_audio_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and audio")

@then('we will log the clientRects and canvas testing time in the saved file')
def we_will_log_the_clientRects_and_canvas_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and canvas")

@then('we will log the clientRects and font testing time in the saved file')
def we_will_log_the_clientRects_and_font_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and font")

@then('we will log the clientRects and navigator testing time in the saved file')
def we_will_log_the_clientRects_and_navigator_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and navigator")

@then('we will log the clientRects and screen testing time in the saved file')
def we_will_log_the_clientRects_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and screen")

@then('we will log the clientRects and webgl testing time in the saved file')
def we_will_log_the_clientRects_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and webgl")

@then('we will log the clientRects and webRTC testing time in the saved file')
def we_will_log_the_clientRects_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and webRTC")