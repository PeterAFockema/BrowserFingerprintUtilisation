from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

# @when('we view the Firefox page with some audio and battery and canvas and clientRects and {last_item} values interference')
# def we_view_the_firefox_page_with_multiple_interferences(context, last_item):
#     # Map the step text wording to the exact extension list string required
#     extension_map = {
#         "font": "font",
#         "navigator": "navigator",
#         "screen": "screen",
#         "webgl": "webgl",
#         "webRTC": "webRTC"
#     }
    
#     # Fallback to the text itself if it matches perfectly
#     extension_name = extension_map.get(last_item, last_item)
    
#     html_puller_firefox = test_manager.html_puller_firefox
#     extensions = ["audio", "battery", "canvas", "clientRects", extension_name]
    
#     soup = BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(extensions), "html.parser")
#     bool(soup.find())
    
#     assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we have a Firefox page which ran the audio and battery and canvas and clientRects and font response')
@then('we have a Firefox page which ran the audio and battery and canvas and clientRects and navigator response')
@then('we have a Firefox page which ran the audio and battery and canvas and clientRects and screen response')
@then('we have a Firefox page which ran the audio and battery and canvas and clientRects and webgl response')
@then('we have a Firefox page which ran the audio and battery and canvas and clientRects and webRTC response')
def we_have_a_firefox_page_which_ran_the_audio_and_battery_and_canvas_and_other_features_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we will log the audio and battery and canvas and clientRects and font testing time in the saved file')
def we_will_log_the_audio_and_battery_and_canvas_and_clientRects_and_font_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and battery and canvas and clientRects and font")

@then('we will log the audio and battery and canvas and clientRects and navigator testing time in the saved file')
def we_will_log_the_audio_and_battery_and_canvas_and_clientRects_and_navigator_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and battery and canvas and clientRects and navigator")

@then('we will log the audio and battery and canvas and clientRects and screen testing time in the saved file')
def we_will_log_the_audio_and_battery_and_canvas_and_clientRects_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and battery and canvas and clientRects and screen")

@then('we will log the audio and battery and canvas and clientRects and webgl testing time in the saved file')
def we_will_log_the_audio_and_battery_and_canvas_and_clientRects_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and battery and canvas and clientRects and webgl")

@then('we will log the audio and battery and canvas and clientRects and webRTC testing time in the saved file')
def we_will_log_the_audio_and_battery_and_canvas_and_clientRects_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and battery and canvas and clientRects and webRTC")

@then('the visitor id for audio and battery and canvas and clientRects and font is saved')
@then('the visitor id for audio and battery and canvas and clientRects and navigator is saved')
@then('the visitor id for audio and battery and canvas and clientRects and screen is saved')
@then('the visitor id for audio and battery and canvas and clientRects and webgl is saved')
@then('the visitor id for audio and battery and canvas and clientRects and webRTC is saved')
def the_firefox_visitor_id_for_audio_and_battery_and_canvas_and_clientRects_and_other_features_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()

@then('the Firefox audio and battery and canvas and clientRects and navigator value has been recorded')
def the_firefox_audio_and_battery_and_canvas_and_clientRects_and_navigator_value_has_been_recorded(context):
    test_manager.html_puller_firefox.save_audio_value()
    #test_manager.html_puller_firefox.save_battery_value() #TODO: If this is available from FingerprintJS, record
    assert test_manager.html_puller_firefox.save_canvas_value()
    #test_manager.html_puller_firefox.save_clientRects_value() #TODO: If this is available from FingerprintJS, record
    #test_manager.html_puller_firefox.save_navigator_value() #TODO: If this is available from FingerprintJS, record

@then('the Firefox audio and battery and canvas and clientRects and screen value has been recorded')
def the_firefox_audio_and_battery_and_canvas_and_clientRects_and_screen_value_has_been_recorded(context):
    test_manager.html_puller_firefox.save_audio_value()
    #test_manager.html_puller_firefox.save_battery_value() #TODO: If this is available from FingerprintJS, record
    test_manager.html_puller_firefox.save_canvas_value()
    #test_manager.html_puller_firefox.save_clientRects_value() #TODO: If this is available from FingerprintJS, record
    assert test_manager.html_puller_firefox.save_screen_resolution_value()

@then('the Firefox audio and battery and canvas and clientRects and webgl value has been recorded')
def the_firefox_audio_and_battery_and_canvas_and_clientRects_and_webgl_value_has_been_recorded(context):
    test_manager.html_puller_firefox.save_audio_value()
    #test_manager.html_puller_firefox.save_battery_value() #TODO: If this is available from FingerprintJS, record
    assert test_manager.html_puller_firefox.save_canvas_value()
    #test_manager.html_puller_firefox.save_clientRects_value() #TODO: If this is available from FingerprintJS, record
    #assert test_manager.html_puller_firefox.save_webgl_value() #TODO: If this is available from FingerprintJS, record

@then('the Firefox audio and battery and canvas and clientRects and webRTC value has been recorded')
def the_firefox_audio_and_battery_and_canvas_and_clientRects_and_webRTC_value_has_been_recorded(context):
    test_manager.html_puller_firefox.save_audio_value()
    #test_manager.html_puller_firefox.save_battery_value() #TODO: If this is available from FingerprintJS, record
    assert test_manager.html_puller_firefox.save_canvas_value()
    #test_manager.html_puller_firefox.save_clientRects_value() #TODO: If this is available from FingerprintJS, record
    #assert test_manager.html_puller_firefox.save_webRTC_value() #TODO: If this is available from FingerprintJS, record