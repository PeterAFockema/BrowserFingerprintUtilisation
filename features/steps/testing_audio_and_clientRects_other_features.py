from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *

test_manager = TestManager()
audio_and_clientRects_increment = 0

'''
The following definitions relate to the Firefox browser.
'''

@when('we view the Firefox page with some audio and clientRects and font values interference')
def we_view_the_firefox_page_with_some_audio_and_clientRects_and_font_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["audio", "clientRects", "font"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and clientRects and navigator values interference')
def we_view_the_firefox_page_with_some_audio_and_clientRects_and_navigator_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["audio", "clientRects", "navigator"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and clientRects and screen values interference')
def we_view_the_firefox_page_with_some_audio_and_clientRects_and_screen_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["audio", "clientRects", "screen"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and clientRects and webgl values interference')
def we_view_the_firefox_page_with_some_audio_and_clientRects_and_webgl_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["audio", "clientRects", "webgl"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and clientRects and webRTC values interference')
def we_view_the_firefox_page_with_some_audio_and_clientRects_and_webRTC_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["audio", "clientRects", "webRTC"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@then('we have a Firefox page which ran the audio and clientRects and font response')
@then('we have a Firefox page which ran the audio and clientRects and navigator response')
@then('we have a Firefox page which ran the audio and clientRects and screen response')
@then('we have a Firefox page which ran the audio and clientRects and webgl response')
@then('we have a Firefox page which ran the audio and clientRects and webRTC response')
def we_have_a_firefox_page_which_ran_the_audio_and_clientRects_and_other_features_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we will log the audio and clientRects and font testing time in the saved file')
def we_will_log_the_audio_and_clientRects_and_font_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and clientRects and font")

@then('we will log the audio and clientRects and navigator testing time in the saved file')
def we_will_log_the_audio_and_clientRects_and_navigator_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and clientRects and navigator")

@then('we will log the audio and clientRects and screen testing time in the saved file')
def we_will_log_the_audio_and_clientRects_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and clientRects and screen")

@then('we will log the audio and clientRects and webgl testing time in the saved file')
def we_will_log_the_audio_and_clientRects_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and clientRects and webgl")

@then('we will log the audio_and_clientRects and webRTC testing time in the saved file')
def we_will_log_the_audio_and_clientRects_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and clientRects and webRTC")

@then('the visitor id for audio and clientRects and font is saved')
@then('the visitor id for audio and clientRects and navigator is saved')
@then('the visitor id for audio and clientRects and screen is saved')
@then('the visitor id for audio and clientRects and webgl is saved')
@then('the visitor id for audio and clientRects and webRTC is saved')
def the_firefox_visitor_id_for_audio_and_clientRects_and_other_features_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()
