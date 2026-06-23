from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('we will log the battery and font and navigator and screen testing time in the saved file')
def we_will_log_the_battery_and_font_and_navigator_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and font and navigator and screen")

@then('we will log the battery and font and navigator and webgl testing time in the saved file')
def we_will_log_the_battery_and_font_and_navigator_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and font and navigator and webgl")

@then('we will log the battery and font and navigator and webRTC testing time in the saved file')
def we_will_log_the_battery_and_font_and_navigator_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and font and navigator and webRTC")

@then('we will log the battery and font and navigator and screen and webgl testing time in the saved file')
def we_will_log_the_battery_and_font_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and font and navigator and screen and webgl")

@then('we will log the battery and font and navigator and screen and webRTC testing time in the saved file')
def we_will_log_the_battery_and_font_and_navigator_and_screen_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and font and navigator and screen and webRTC")

@then('we will log the battery and font and navigator and webgl and webRTC testing time in the saved file')
def we_will_log_the_battery_and_font_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and font and navigator and webgl and webRTC")

@then('we will log the battery and font and font testing time in the saved file')
def we_will_log_the_battery_and_font_and_font_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and font and font")

@then('we will log the battery and font and navigator testing time in the saved file')
def we_will_log_the_battery_and_font_and_navigator_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and font and navigator")

@then('we will log the battery and font and screen testing time in the saved file')
def we_will_log_the_battery_and_font_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and font and screen")

@then('we will log the battery and font and webgl testing time in the saved file')
def we_will_log_the_battery_and_font_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and font and webgl")

@then('we will log the battery and font and webRTC testing time in the saved file')
def we_will_log_the_battery_and_font_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and font and webRTC")

@then('we will log the battery and font and screen and webgl testing time in the saved file')
def we_will_log_the_battery_and_font_and_screen_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and font and screen and webgl")

@then('we will log the battery and font and screen and webRTC testing time in the saved file')
def we_will_log_the_battery_and_font_and_screen_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and font and screen and webRTC")

@then('we will log the battery and font and webgl and webRTC testing time in the saved file')
def we_will_log_the_battery_and_font_and_webgl_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and font and webgl and webRTC")

@then('we will log the battery and navigator and screen testing time in the saved file')
def we_will_log_the_battery_and_navigator_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and navigator and screen")

@then('we will log the battery and navigator and webgl testing time in the saved file')
def we_will_log_the_battery_and_navigator_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and navigator and webgl")

@then('we will log the battery and navigator and webRTC testing time in the saved file')
def we_will_log_the_battery_and_navigator_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and navigator and webRTC")

@then('we will log the battery and navigator and screen and webgl and webgl testing time in the saved file')
def we_will_log_the_battery_and_navigator_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and navigator and screen and webgl and webgl")

@then('we will log the battery and audio testing time in the saved file')
def we_will_log_the_battery_and_audio_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and battery")

@then('we will log the battery and canvas testing time in the saved file')
def we_will_log_the_battery_and_canvas_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and canvas")

@then('we will log the battery and clientRects testing time in the saved file')
def we_will_log_the_battery_and_clientRects_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and clientRects")

@then('we will log the battery and font testing time in the saved file')
def we_will_log_the_battery_and_font_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and font")

@then('we will log the battery and navigator testing time in the saved file')
def we_will_log_the_battery_and_navigator_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and navigator")

@then('we will log the battery and screen testing time in the saved file')
def we_will_log_the_battery_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and screen")

@then('we will log the battery and webgl testing time in the saved file')
def we_will_log_the_battery_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and webgl")

@then('we will log the battery and webRTC testing time in the saved file')
def we_will_log_the_battery_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and webRTC")

@then('we will log the battery and screen and webgl testing time in the saved file')
def we_will_log_the_battery_and_screen_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and screen and webgl")

@then('we will log the battery and screen and webRTC testing time in the saved file')
def we_will_log_the_battery_and_screen_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and screen and webRTC")

@then('we will log the battery and webgl and webRTC testing time in the saved file')
def we_will_log_the_battery_and_webgl_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and webgl and webRTC")

@then('we will log the battery testing time in the saved file')
def we_will_log_the_battery_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery")

@then('we will log the canvas and clientRects and font and navigator and screen testing time in the saved file')
def we_will_log_the_canvas_and_clientRects_and_font_and_navigator_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and clientRects and font and navigator and screen")

@then('we will log the canvas and clientRects and font and navigator and webgl testing time in the saved file')
def we_will_log_the_canvas_and_clientRects_and_font_and_navigator_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and clientRects and font and navigator and webgl")

@then('we will log the canvas and clientRects and font and navigator and webRTC testing time in the saved file')
def we_will_log_the_canvas_and_clientRects_and_font_and_navigator_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and clientRects and font and navigator and webRTC")

@then('we will log the canvas and clientRects and font and navigator testing time in the saved file')
def we_will_log_the_canvas_and_clientRects_and_font_navigator_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and clientRects and font and navigator")

@then('we will log the canvas and clientRects and font and screen testing time in the saved file')
def we_will_log_the_canvas_and_clientRects_and_font_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and clientRects and font and screen")

@then('we will log the canvas and clientRects and font and webgl testing time in the saved file')
def we_will_log_the_canvas_and_clientRects_and_font_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and clientRects and font and webgl")

@then('we will log the canvas and clientRects and font and webRTC testing time in the saved file')
def we_will_log_the_canvas_and_clientRects_and_font_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and clientRects and font and webRTC")

@then('we will log the canvas and clientRects and font and screen and webgl testing time in the saved file')
def we_will_log_the_canvas_and_clientRects_and_font_and_screen_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and clientRects and font and screen and webgl")

@then('we will log the canvas and clientRects and font and screen and webRTC testing time in the saved file')
def we_will_log_the_canvas_and_clientRects_and_font_and_screen_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and clientRects and font and screen and webRTC")

@then('we will log the canvas and clientRects and font and webgl and webRTC testing time in the saved file')
def we_will_log_the_canvas_and_clientRects_and_font_and_webgl_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and clientRects and font and webgl and webRTC")

@then('we will log the canvas and clientRects and navigator and screen testing time in the saved file')
def we_will_log_the_canvas_and_clientRects_and_navigator_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and clientRects and navigator and screen")

@then('we will log the canvas and clientRects and navigator and webgl testing time in the saved file')
def we_will_log_the_canvas_and_clientRects_and_navigator_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and clientRects and navigator and webgl")

@then('we will log the canvas and clientRects and navigator and webRTC testing time in the saved file')
def we_will_log_the_canvas_and_clientRects_and_navigator_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and clientRects and navigator and webRTC")

@then('we will log the canvas and clientRects and screen and screen testing time in the saved file')
def we_will_log_the_canvas_and_clientRects_and_screen_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and clientRects and screen and screen")

@then('we will log the canvas and clientRects and screen and webgl testing time in the saved file')
def we_will_log_the_canvas_and_clientRects_and_screen_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and clientRects and screen and webgl")

@then('we will log the canvas and clientRects and screen and webRTC testing time in the saved file')
def we_will_log_the_canvas_and_clientRects_and_screen_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and clientRects and screen and webRTC")

@then('we will log the canvas and clientRects and webgl and webRTC testing time in the saved file')
def we_will_log_the_canvas_and_clientRects_and_webgl_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and clientRects and webgl and webRTC")

@then('we will log the canvas and font and screen testing time in the saved file')
def we_will_log_the_canvas_and_font_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and font and screen")

@then('we will log the no offsetHeight and offsetWidth testing time in the saved file')
def we_will_log_the_no_offsetHeight_and_offsetWidth_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("no offsetHeight and offsetWidth")

@then('we will log the offsetHeight testing time in the saved file')
def we_will_log_the_offsetHeight_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("offsetHeight")

@then('we will log the offsetWidth testing time in the saved file')
def we_will_log_the_offsetWidth_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("offsetWidth")

@then('we will log the offsetHeight and offsetWidth testing time in the saved file')
def we_will_log_the_offsetHeight_and_offsetWidth_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("offsetHeight and offsetWidth")

    @then('we will log the navigator and battery testing time in the saved file')
def we_will_log_the_navigator_and_battery_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("navigator and battery")

@then('we will log the navigator and audio testing time in the saved file')
def we_will_log_the_navigator_and_audio_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("navigator and audio")

@then('we will log the navigator and canvas testing time in the saved file')
def we_will_log_the_navigator_and_canvas_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("navigator and canvas")

@then('we will log the navigator and clientRect testing time in the saved file')
def we_will_log_the_navigator_and_clientRect_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("navigator and clientRect")

@then('we will log the navigator and font testing time in the saved file')
def we_will_log_the_navigator_and_font_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("navigator and font")

@then('we will log the navigator and screen testing time in the saved file')
def we_will_log_the_navigator_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("navigator and screen")

@then('we will log the navigator and webgl testing time in the saved file')
def we_will_log_the_navigator_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("navigator and webgl")

@then('we will log the navigator and webRTC testing time in the saved file')
def we_will_log_the_navigator_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("navigator and webRTC")

@then('we will log the no screen testing time variance in the saved file')
def we_will_log_the_no_screen_time_variance_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("no screen")

@then('we will log the screen testing time in the saved file')
def we_will_log_the_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("screen")

@then('we will log the no parameter and buffer testing time in the saved file')
def we_will_log_the_no_parameter_and_buffer_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("no parameter and buffer")

@then('we will log the parameter testing time in the saved file')
def we_will_log_the_parameter_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("parameter")

@then('we will log the buffer testing time in the saved file')
def we_will_log_the_buffer_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("buffer")

@then('we will log the parameter and buffer values testing time in the saved file')
def we_will_log_the_parameter_and_buffer_values_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("parameter and buffer")

@then('we will log the webgl and battery testing time in the saved file')
def we_will_log_the_webgl_and_battery_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("webgl and battery")

@then('we will log the webgl and audio testing time in the saved file')
def we_will_log_the_webgl_and_audio_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("webgl and audio")

@then('we will log the webgl and canvas testing time in the saved file')
def we_will_log_the_webgl_and_canvas_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("webgl and canvas")

@then('we will log the webgl and clientRect testing time in the saved file')
def we_will_log_the_webgl_and_clientRect_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("webgl and clientRect")

@then('we will log the webgl and font testing time in the saved file')
def we_will_log_the_webgl_and_font_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("webgl and font")

@then('we will log the webgl and navigator testing time in the saved file')
def we_will_log_the_webgl_and_navigator_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("webgl and navigator")

@then('we will log the webgl and screen testing time in the saved file')
def we_will_log_the_webgl_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("webgl and screen")

@then('we will log the webgl and webRTC testing time in the saved file')
def we_will_log_the_webgl_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("webgl and webRTC")

@then('we will log the webrtc and battery testing time in the saved file')
def we_will_log_the_webrtc_and_battery_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("webrtc and battery")

@then('we will log the webrtc and audio testing time in the saved file')
def we_will_log_the_webrtc_and_audio_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("webrtc and audio")

@then('we will log the webrtc and canvas testing time in the saved file')
def we_will_log_the_webrtc_and_canvas_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("webrtc and canvas")

@then('we will log the webrtc and clientRect testing time in the saved file')
def we_will_log_the_webrtc_and_clientRect_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("webrtc and clientRect")

@then('we will log the webrtc and font testing time in the saved file')
def we_will_log_the_webrtc_and_font_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("webrtc and font")

@then('we will log the webrtc and navigator testing time in the saved file')
def we_will_log_the_webrtc_and_navigator_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("webrtc and navigator")

@then('we will log the webrtc and screen testing time in the saved file')
def we_will_log_the_webrtc_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("webrtc and screen")

@then('we will log the webrtc and webgl testing time in the saved file')
def we_will_log_the_webrtc_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("webrtc and webgl")

@then('we will log the webgl testing time in the saved file')
def we_will_log_the_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("webgl")

@then('we will log the no availHeight or availWidth or colorDepth values interference testing time in the saved file')
def we_will_log_the_no_availHeight_or_availWidth_or_colorDepth_values_interference_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("no availHeight or availWidth or colorDepth values interference")

@then('we will log the availHeight testing time in the saved file')
def we_will_log_the_availHeight_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("availHeight values interference")

@then('we will log the availWidth testing time in the saved file')
def we_will_log_the_availWidth_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("availWidth values interference")

@then('we will log the colorDepth testing time in the saved file')
def we_will_log_the_colorDepth_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("colorDepth values interference")

@then('we will log the devicePixelRatio testing time in the saved file')
def we_will_log_the_devicePixelRatio_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("devicePixelRatio values interference")
    
@then('we will log the availHeight and availWidth values testing time in the saved file')
def we_will_log_the_availHeight_and_availWidth_values_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("availHeight and availWidth values interference")

@then('we will log the availHeight and colorDepth values testing time in the saved file')
def we_will_log_the_availHeight_and_colorDepth_values_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("availHeight and colorDepth values interference")

@then('we will log the availHeight and devicePixelRatio values testing time in the saved file')
def we_will_log_the_availHeight_and_devicePixelRatio_values_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("availHeight and devicePixelRatio values interference")

@then('we will log the availWidth and colorDepth values testing time in the saved file')
def we_will_log_the_availWidth_and_colorDepth_values_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("availWidth and colorDepth values interference")

@then('we will log the availWidth and devicePixelRatio values testing time in the saved file')
def we_will_log_the_availWidth_and_devicePixelRatio_values_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("availWidth and devicePixelRatio values interference")

@then('we will log the colorDepth and devicePixelRatio values testing time in the saved file')
def we_will_log_the_colorDepth_and_devicePixelRatio_values_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("colorDepth and devicePixelRatio values interference")

@then('we will log the availHeight and availWidth and colorDepth values testing time in the saved file')
def we_will_log_the_availHeight_and_availWidth_and_colorDepth_values_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("availHeight and availWidth and colorDepth values interference")

@then('we will log the availHeight and availWidth and devicePixelRatio values testing time in the saved file')
def we_will_log_the_availHeight_and_availWidth_and_devicePixelRatio_values_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("availHeight and availWidth and devicePixelRatio values interference")

@then('we will log the availHeight and devicePixelRatio and colorDepth values testing time in the saved file')
def we_will_log_the_availHeight_and_devicePixelRatio_and_colorDepth_values_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("availHeight and devicePixelRatio and colorDepth values interference")

@then('we will log the availWidth and devicePixelRatio and colorDepth values testing time in the saved file')
def we_will_log_the_availWidth_and_devicePixelRatio_and_colorDepth_values_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("availWidth and devicePixelRatio and colorDepth values interference")

@then('we will log the availHeight and availWidth and devicePixelRatio and colorDepth values testing time in the saved file')
def we_will_log_the_availHeight_and_availWidth_and_devicePixelRatio_and_colorDepth_values_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("availHeight and availWidth and devicePixelRatio and colorDepth values interference")


@then('we will log the screen and battery testing time in the saved file')
def we_will_log_the_screen_and_battery_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("screen and battery")

@then('we will log the screen and audio testing time in the saved file')
def we_will_log_the_screen_and_audio_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("screen and audio")

@then('we will log the screen and canvas testing time in the saved file')
def we_will_log_the_screen_and_canvas_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("screen and canvas")

@then('we will log the screen and clientRect testing time in the saved file')
def we_will_log_the_screen_and_clientRect_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("screen and clientRect")

@then('we will log the screen and font testing time in the saved file')
def we_will_log_the_screen_and_font_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("screen and font")

@then('we will log the screen and navigator testing time in the saved file')
def we_will_log_the_screen_and_navigator_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("screen and navigator")

@then('we will log the screen and webgl testing time in the saved file')
def we_will_log_the_screen_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("screen and webgl")

@then('we will log the screen and webRTC testing time in the saved file')
def we_will_log_the_screen_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("screen and webRTC")

@then('we will log the navigator testing time in the saved file')
def we_will_log_the_navigator_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("navigator")

@then('we will log the navigator and screen and webgl and webRTC testing time in the saved file')
def we_will_log_the_navigator_and_screen_and_webgl_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("navigator and screen and webgl and webRTC")

@then('we will log the no toBlob and toDataURL testing time in the saved file')
def we_will_log_the_no_toBlob_and_toDataURL_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("no toBlob and toDataURL")

@then('we will log the toBlob testing time in the saved file')
def we_will_log_the_toBlob_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("toBlob")

@then('we will log the toDataURL testing time in the saved file')
def we_will_log_the_toDataURL_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("toDataURL")

@then('we will log the toBlob and toDataURL values testing time in the saved file')
def we_will_log_the_toBlob_and_toDataURL_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("toBlob and toDataURL")

@then('we will log the no font testing time in the saved file')
def we_will_log_the_no_font_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("no font")

@then('we will log the font testing time in the saved file')
def we_will_log_the_font_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("font")

@then('we will log the font and battery testing time in the saved file')
def we_will_log_the_font_and_battery_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("font and battery")

@then('we will log the font and audio testing time in the saved file')
def we_will_log_the_font_and_audio_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("font and audio")

@then('we will log the font and canvas testing time in the saved file')
def we_will_log_the_font_and_canvas_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("font and canvas")

@then('we will log the font and clientRect testing time in the saved file')
def we_will_log_the_font_and_clientRect_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("font and clientRect")

@then('we will log the font and navigator testing time in the saved file')
def we_will_log_the_font_and_navigator_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("font and navigator")

@then('we will log the font and screen testing time in the saved file')
def we_will_log_the_font_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("font and screen")

@then('we will log the font and webgl testing time in the saved file')
def we_will_log_the_font_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("font and webgl")

@then('we will log the font and webRTC testing time in the saved file')
def we_will_log_the_font_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("font and webRTC")

@then('we will log the font and navigator and webgl and webRTC testing time in the saved file')
def we_will_log_the_font_and_navigator_and_webgl_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("font and navigator and webgl and webRTC")

@then('we will log the audio and navigator and screen and webgl testing time in the saved file')
def we_will_log_the_audio_and_navigator_and_screen_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and navigator and screen and webgl")

@then('we will log the audio and navigator and screen and webRTC testing time in the saved file')
def we_will_log_the_audio_and_navigator_and_screen_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and navigator and screen and webRTC")

@then('we will log the font and navigator and screen and webgl and webRTC testing time in the saved file')
def we_will_log_the_font_and_navigator_and_screen_and_webgl_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("font and navigator and screen and webgl and webRTC")

@then('we will log the font and navigator and screen and webgl testing time in the saved file')
def we_will_log_the_font_and_navigator_and_screen_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("font and navigator and screen and webgl")

@then('we will log the font and navigator and screen and webRTC testing time in the saved file')
def we_will_log_the_font_and_navigator_and_screen_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("font and navigator and screen and webRTC")

@then('we will log the clientRects testing time in the saved file')
def we_will_log_the_clientRects_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects")


@then('we will log the clientRects and battery testing time in the saved file')
def we_will_log_the_clientRects_and_battery_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and battery")

@then('we will log the clientRects and audio testing time in the saved file')
def we_will_log_the_clientRects_and_audio_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and audio")

@then('we will log the clientRects and canvas testing time in the saved file')
def we_will_log_the_clientRects_and_canvas_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and canvas")

@then('we will log the clientRects and font testing time in the saved file')
def we_will_log_the_clientRects_and_font_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and font")

@then('we will log the clientRects and navigator testing time in the saved file')
def we_will_log_the_clientRects_and_navigator_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and navigator")

@then('we will log the clientRects and screen testing time in the saved file')
def we_will_log_the_clientRects_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and screen")

@then('we will log the clientRects and webgl testing time in the saved file')
def we_will_log_the_clientRects_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and webgl")

@then('we will log the clientRects and webRTC testing time in the saved file')
def we_will_log_the_clientRects_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and webRTC")

@then('we will log the clientRects and font and webgl and webRTC testing time in the saved file')
def we_will_log_the_clientRects_and_font_and_webgl_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and font and webgl and webRTC")

@then('we will log the clientRects and font and navigator and webgl and webRTC testing time in the saved file')
def we_will_log_the_clientRects_and_font_and_navigator_and_webgl_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and font and navigator and webgl and webRTC")


@then('we will log the clientRects and font and screen and webgl testing time in the saved file')
def we_will_log_the_clientRects_and_font_and_screen_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and font and screen and webgl")

@then('we will log the clientRects and font and screen and webRTC testing time in the saved file')
def we_will_log_the_clientRects_and_font_and_screen_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and font and screen and webRTC")


@then('we will log the clientRects and font and navigator and screen and webgl testing time in the saved file')
def we_will_log_the_clientRects_and_font_and_navigator_and_screen_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and font and navigator and screen and webgl")

@then('we will log the clientRects and font and navigator and screen and webRTC testing time in the saved file')
def we_will_log_the_clientRects_and_font_and_navigator_and_screen_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and font and navigator and screen and webRTC")

@then('we will log the canvas and battery testing time in the saved file')
def we_will_log_the_canvas_and_battery_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and battery")

@then('we will log the canvas and audio testing time in the saved file')
def we_will_log_the_canvas_and_audio_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and audio")

@then('we will log the canvas and clientRects testing time in the saved file')
def we_will_log_the_canvas_and_clientRects_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and clientRects")

@then('we will log the canvas and font testing time in the saved file')
def we_will_log_the_canvas_and_font_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and font")

@then('we will log the canvas and navigator testing time in the saved file')
def we_will_log_the_canvas_and_navigator_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and navigator")

@then('we will log the canvas and screen testing time in the saved file')
def we_will_log_the_canvas_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and screen")

@then('we will log the canvas and webgl testing time in the saved file')
def we_will_log_the_canvas_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and webgl")

@then('we will log the canvas and webRTC testing time in the saved file')
def we_will_log_the_canvas_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and webRTC")

@then('we will log the clientRects and font and navigator and screen testing time in the saved file')
def we_will_log_the_clientRects_and_font_and_navigator_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and font and navigator and screen")

@then('we will log the clientRects and font and navigator and webgl testing time in the saved file')
def we_will_log_the_clientRects_and_font_and_navigator_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and font and navigator and webgl")

@then('we will log the clientRects and font and navigator and webRTC testing time in the saved file')
def we_will_log_the_clientRects_and_font_and_navigator_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and font and navigator and webRTC")
