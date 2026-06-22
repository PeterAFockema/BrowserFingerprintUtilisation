from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('we have a Firefox page which ran the audio and canvas and clientRects and clientRects response')
@then('we have a Firefox page which ran the audio and canvas and clientRects and font response')
@then('we have a Firefox page which ran the audio and canvas and clientRects and navigator response')
@then('we have a Firefox page which ran the audio and canvas and clientRects and screen response')
@then('we have a Firefox page which ran the audio and canvas and clientRects and webgl response')
@then('we have a Firefox page which ran the audio and canvas and clientRects and webRTC response')
def we_have_a_firefox_page_which_ran_the_audio_and_canvas_and_clientRects_and_other_features_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we will log the audio and canvas and clientRects and font testing time in the saved file')
def we_will_log_the_audio_and_canvas_and_clientRects_font_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and canvas and clientRects and font")

@then('we will log the audio and canvas and clientRects and navigator testing time in the saved file')
def we_will_log_the_audio_and_canvas_and_clientRects_navigator_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and canvas and clientRects and navigator")

@then('we will log the audio and canvas and clientRects and screen testing time in the saved file')
def we_will_log_the_audio_and_canvas_and_clientRects_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and canvas and clientRects and screen")

@then('we will log the audio and canvas and clientRects and webgl testing time in the saved file')
def we_will_log_the_audio_and_canvas_and_clientRects_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and canvas and clientRects and webgl")

@then('we will log the audio and canvas and clientRects and webRTC testing time in the saved file')
def we_will_log_the_audio_and_canvas_and_clientRects_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and canvas and clientRects and webRTC")
