from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *

test_manager = TestManager()
audio_increment = 0

'''
The following definitions relate to the Firefox browser.
'''

@when('we view the Firefox page with some audio and battery values interference')
def we_view_the_firefox_page_with_some_audio_and_battery_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["audio", "audio"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and canvas values interference')
def we_view_the_firefox_page_with_some_audio_and_canvas_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["audio", "canvas"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and clientRects values interference')
def we_view_the_firefox_page_with_some_audio_and_clientRects_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["audio", "clientRects"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and font values interference')
def we_view_the_firefox_page_with_some_audio_and_font_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["audio", "font"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and navigator values interference')
def we_view_the_firefox_page_with_some_audio_and_navigator_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["audio", "navigator"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and screen values interference')
def we_view_the_firefox_page_with_some_audio_and_screen_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["audio", "screen"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and webgl values interference')
def we_view_the_firefox_page_with_some_audio_and_webgl_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["audio", "webgl"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and webRTC values interference')
def we_view_the_firefox_page_with_some_audio_and_webRTC_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["audio", "webRTC"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

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
