from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *

test_manager = TestManager()
audio_and_battery_and_canvas_and_webgl_increment = 0

'''
The following definitions relate to the Firefox browser.
'''

@when('we view the Firefox page with some audio and battery and canvas and webgl and webRTC values interference')
def we_view_the_firefox_page_with_some_audio_and_battery_and_canvas_and_webRTC_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["audio", "battery", "canvas", "webgl", "webRTC"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@then('we have a Firefox page which ran the audio and battery and canvas and webgl and webRTC response')
def we_have_a_firefox_page_which_ran_the_audio_and_battery_and_canvas_and_other_features_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we will log the audio and battery and canvas and webgl and webRTC testing time in the saved file')
def we_will_log_the_audio_and_battery_and_canvas_and_webgl_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and battery and canvas and webgl and webRTC")

@then('the visitor id for audio and battery and canvas and webgl and webRTC is saved')
def the_firefox_visitor_id_for_audio_and_battery_and_canvas_and_webgl_and_other_features_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()
