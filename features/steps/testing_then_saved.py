from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser for a single value.
'''

@then('the Firefox audio value is saved')
def the_firefox_audio_value_has_been_recorded(context):
    test_manager.html_puller_firefox.save_audio_value()

@then('the Firefox battery value is saved')
def the_firefox_battery_value_has_been_recorded(context):
    print("TODO: look at how to extract battery value (if available) from FingerprintJS")
    # assert test_manager.html_puller_firefox.save_battery_value() #TODO: If this is available from FingerprintJS, record

@then('the Firefox clientRects value is saved')
def the_firefox_clientRects_value_has_been_recorded(context):
    print("TODO: look at how to extract clientRects value (if available) from FingerprintJS")
    # assert test_manager.html_puller_firefox.save_clientRects_value() #TODO: If this is available from FingerprintJS, record

@then('the Firefox font value is saved')
def the_firefox_font_value_has_been_recorded(context):
    test_manager.html_puller_firefox.save_fonts_value()

@then('the Firefox navigator value is saved')
def the_firefox_navigator_value_is_saved(context):
    print("TODO: look at how to extract navigator value (if available) from FingerprintJS")
    # assert test_manager.html_puller_firefox.save_navigator_value() #TODO: If this is available from FingerprintJS, record

@then('the Firefox screen value is saved')
def the_firefox_screen_value_has_been_recorded(context):
    test_manager.html_puller_firefox.save_screen_resolution_value()

'''
The following is for multiple values to be saved
'''

@then('the Firefox audio and battery and screen value is saved')
def the_firefox_audio_and_battery_and_screen_value_is_saved(context):
    test_manager.html_puller_firefox.save_audio_value()
    test_manager.html_puller_chrome.save_battery_value() #TODO: See if this can be extracted from FingerprintJS
    assert test_manager.html_puller_firefox.save_screen_resolution_value()

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