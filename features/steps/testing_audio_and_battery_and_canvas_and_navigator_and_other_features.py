from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

# test_manager = TestManager()
# audio_and_battery_and_canvas_and_navigator_increment = 0

'''
The following definitions relate to the Firefox browser.
'''

@when('we view the Firefox page with some audio and battery and canvas and navigator and screen values interference')
def we_view_the_firefox_page_with_some_audio_and_battery_and_canvas_and_screen_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "battery", "canvas", "navigator", "screen"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and battery and canvas and navigator and webgl values interference')
def we_view_the_firefox_page_with_some_audio_and_battery_and_canvas_and_webgl_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "battery", "canvas", "navigator",  "webgl"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and battery and canvas and navigator and webRTC values interference')
def we_view_the_firefox_page_with_some_audio_and_battery_and_canvas_and_webRTC_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "battery", "canvas", "navigator", "webRTC"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@then('we have a Firefox page which ran the audio and battery and canvas and navigator and screen response')
@then('we have a Firefox page which ran the audio and battery and canvas and navigator and webgl response')
@then('we have a Firefox page which ran the audio and battery and canvas and navigator and webRTC response')
def we_have_a_firefox_page_which_ran_the_audio_and_battery_and_canvas_and_other_features_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we will log the audio and battery and canvas and navigator and screen testing time in the saved file')
def we_will_log_the_audio_and_battery_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and battery and canvas and navigator and screen")

@then('we will log the audio and battery and canvas and navigator and webgl testing time in the saved file')
def we_will_log_the_audio_and_battery_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and battery and canvas and navigator and webgl")

@then('we will log the audio and battery and canvas and navigator and webRTC testing time in the saved file')
def we_will_log_the_audio_and_battery_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and battery and canvas and navigator and webRTC")

@then('the visitor id for audio and battery and canvas and navigator and screen is saved')
@then('the visitor id for audio and battery and canvas and navigator and webgl is saved')
@then('the visitor id for audio and battery and canvas and navigator and webRTC is saved')
def the_firefox_visitor_id_for_audio_and_battery_and_canvas_and_navigator_and_other_features_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()

@then('the Firefox navigator value is saved')
def the_firefox_navigator_value_is_saved(context):
    print("TODO: look at how to extract navigator value (if available) from FingerprintJS")
    # assert test_manager.html_puller_firefox.save_navigator_value() #TODO: If this is available from FingerprintJS, record

@then('the Firefox audio and battery and canvas and navigator value is saved')
def the_firefox_audio_and_battery_and_canvas_and_navigator_value_is_saved(context):
    test_manager.html_puller_firefox.save_audio_value()
    #test_manager.html_puller_firefox.save_battery_value() #TODO: If this is available from FingerprintJS, record
    test_manager.html_puller_firefox.save_canvas_value()
    assert test_manager.html_puller_firefox.save_fonts_value()
    # assert test_manager.html_puller_firefox.save_navigator_value() #TODO: If this is available from FingerprintJS, record

@then('the Firefox audio and battery and canvas and navigator and webgl value is saved')
def the_firefox_audio_and_battery_and_canvas_and_navigator_and_webgl_value_is_saved(context):
    test_manager.html_puller_firefox.save_audio_value()
    #test_manager.html_puller_firefox.save_battery_value() #TODO: If this is available from FingerprintJS, record
    test_manager.html_puller_firefox.save_canvas_value()
    assert test_manager.html_puller_firefox.save_web_gl_value()
    # assert test_manager.html_puller_firefox.save_navigator_value() #TODO: If this is available from FingerprintJS, record