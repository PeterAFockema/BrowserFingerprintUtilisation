from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

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