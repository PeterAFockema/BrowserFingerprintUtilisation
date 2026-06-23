from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

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
