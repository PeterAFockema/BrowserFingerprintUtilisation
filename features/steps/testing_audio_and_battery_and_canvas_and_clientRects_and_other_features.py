from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

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