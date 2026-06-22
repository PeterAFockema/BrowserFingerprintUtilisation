from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('we have a Firefox page which ran the audio and battery response')
@then('we have a Firefox page which ran the audio and canvas response')
@then('we have a Firefox page which ran the audio and clientRects response')
@then('we have a Firefox page which ran the audio and font response')
@then('we have a Firefox page which ran the audio and navigator response')
@then('we have a Firefox page which ran the audio and screen response')
@then('we have a Firefox page which ran the audio and webgl response')
@then('we have a Firefox page which ran the audio and webRTC response')
def we_have_a_firefox_page_which_ran_the_audio_and_other_features_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

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

@then('the visitor id for audio and battery is saved')
@then('the visitor id for audio and canvas is saved')
@then('the visitor id for audio and clientRects is saved')
@then('the visitor id for audio and font is saved')
@then('the visitor id for audio and navigator is saved')
@then('the visitor id for audio and screen is saved')
@then('the visitor id for audio and webgl is saved')
@then('the visitor id for audio and webRTC is saved')
def the_firefox_visitor_id_for_audio_and_other_features_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()
