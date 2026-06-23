from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

# @then('the Firefox audio value has been recorded')
# def the_firefox_audio_value_has_been_recorded(context):
#     assert test_manager.html_puller_firefox.get_audio_value() != None # TODO: Create a get_audio_value() function

# @then('the Firefox battery value has been recorded')
# def the_firefox_battery_value_has_been_recorded(context):
#     assert test_manager.html_puller_firefox.get_battery_value() != None # TODO: Create a get_battery_value() function

@then('the Firefox canvas value has been recorded')
def the_firefox_canvas_value_has_been_recorded(context):
    assert test_manager.html_puller_firefox.get_canvas_value() != None

# @then('the Firefox clientRects value has been recorded')
# def the_firefox_clientRects_value_has_been_recorded(context):
#     assert test_manager.html_puller_firefox.get_client_value() != None # TODO: Create a get_client_value() function
    
@then('the Firefox font value has been recorded')
def the_firefox_font_value_has_been_recorded(context):
    assert test_manager.html_puller_firefox.get_fonts_value() != None

@then('the Firefox screen value has been recorded')
def the_firefox_screen_value_has_been_recorded(context):
    assert test_manager.html_puller_firefox.get_screen_resolution_value() != None

# @then('the Firefox navigator value has been recorded')
# def the_firefox_navigator_value_has_been_recorded(context):
#     assert test_manager.html_puller_firefox.get_navigator_value() != None # TODO: Create a get_navigator_value() function
    
@then('the Firefox webgl value has been recorded')
def the_firefox_webgl_value_has_been_recorded(context):
    assert test_manager.html_puller_firefox.get_web_gl_value() != None
    
@then('the Firefox webRTC value has been recorded')
def the_firefox_webRTC_value_has_been_recorded(context):
    assert test_manager.html_puller_firefox.get_web_gl_value() != None