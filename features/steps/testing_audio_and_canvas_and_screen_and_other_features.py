from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('we have a Firefox page which ran the audio and canvas and screen and screen response')
@then('we have a Firefox page which ran the audio and canvas and screen and webgl response')
@then('we have a Firefox page which ran the audio and canvas and screen and webRTC response')
def we_have_a_firefox_page_which_ran_the_audio_and_canvas_and_screen_and_other_features_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we will log the audio and canvas and screen and webgl testing time in the saved file')
def we_will_log_the_audio_and_canvas_and_screen_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and canvas and screen and webgl")

@then('we will log the audio and canvas and screen and webRTC testing time in the saved file')
def we_will_log_the_audio_and_canvas_and_screen_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and canvas and screen and webRTC")

@then('the visitor id for audio and canvas and screen and webgl is saved')
@then('the visitor id for audio and canvas and screen and webRTC is saved')
def the_firefox_visitor_id_for_audio_and_canvas_and_screen_and_other_features_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()
