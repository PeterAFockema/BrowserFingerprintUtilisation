from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('we have a Firefox page which ran the audio and battery and canvas and font and navigator response')
@then('we have a Firefox page which ran the audio and battery and canvas and font and screen response')
@then('we have a Firefox page which ran the audio and battery and canvas and font and webgl response')
@then('we have a Firefox page which ran the audio and battery and canvas and font and webRTC response')
def we_have_a_firefox_page_which_ran_the_audio_and_battery_and_canvas_and_other_features_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we will log the audio and battery and canvas and font and navigator testing time in the saved file')
def we_will_log_the_audio_and_battery_and_navigator_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and battery and canvas and font and navigator")

@then('we will log the audio and battery and canvas and font and screen testing time in the saved file')
def we_will_log_the_audio_and_battery_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and battery and canvas and font and screen")

@then('we will log the audio and battery and canvas and font and webgl testing time in the saved file')
def we_will_log_the_audio_and_battery_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and battery and canvas and font and webgl")

@then('we will log the audio and battery and canvas and font and webRTC testing time in the saved file')
def we_will_log_the_audio_and_battery_and_canvas_and_font_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and battery and canvas and font and webRTC")

@then('the Firefox audio and battery and canvas and font and navigator value has been recorded')
def the_firefox_audio_and_battery_and_canvas_and_font_and_navigator_value_has_been_recorded(context):
    test_manager.html_puller_firefox.save_audio_value()
    #test_manager.html_puller_firefox.save_battery_value() #TODO: If this is available from FingerprintJS, record
    test_manager.html_puller_firefox.save_canvas_value()
    #test_manager.html_puller_firefox.save_webRTC_value() #TODO: If this is available from FingerprintJS, record
    assert test_manager.html_puller_firefox.save_fonts_value() #TODO: If this is available from FingerprintJS, record
    #assert test_manager.html_puller_firefox.save_navigator_value() #TODO: If this is available from FingerprintJS, record

@then('the Firefox audio and battery and canvas and font and screen value has been recorded')
def the_firefox_audio_and_battery_and_canvas_and_font_and_screen_value_has_been_recorded(context):
    test_manager.html_puller_firefox.save_audio_value()
    #test_manager.html_puller_firefox.save_battery_value() #TODO: If this is available from FingerprintJS, record
    test_manager.html_puller_firefox.save_canvas_value()
    test_manager.html_puller_firefox.save_fonts_value() #TODO: If this is available from FingerprintJS, record
    assert test_manager.html_puller_firefox.save_screen_resolution_value()

@then('the Firefox audio and battery and canvas and font value is saved')
def the_firefox_audio_and_battery_and_canvas_and_font_value_is_saved(context):
    test_manager.html_puller_firefox.save_audio_value()
    #test_manager.html_puller_firefox.save_battery_value() #TODO: If this is available from FingerprintJS, record
    test_manager.html_puller_firefox.save_canvas_value()
    assert test_manager.html_puller_firefox.save_fonts_value() #TODO: If this is available from FingerprintJS, record
