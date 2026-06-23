from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser and only a single extension.
'''

@when('we view the Firefox page with some audio values interference')
def we_view_the_firefox_page_with_some_audio_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_string("audio"), "html.parser").find())
    test_manager.html_puller_chrome= html_puller_firefox
    assert test_manager.html_puller_chrome.html_source != "<html></html>" 

@when('we view the Firefox page with some battery values interference')
def we_view_the_firefox_page_with_some_battery_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_string("battery"), "html.parser").find())
    test_manager.html_puller_chrome= html_puller_firefox
    assert test_manager.html_puller_chrome.html_source != "<html></html>" 

@when('we view the Firefox page with some canvas values interference')
def we_view_the_firefox_page_with_some_canvas_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_canvas_extension(), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some clientRects values interference')
def we_view_the_firefox_page_with_some_clientRects_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_string("clientRects"), "html.parser").find())
    test_manager.html_puller_chrome= html_puller_firefox
    assert test_manager.html_puller_chrome.html_source != "<html></html>" 

@when('we view the Firefox page with some toBlob values interference')
def we_view_the_firefox_page_with_some_toBlob_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_string("toBlob"), "html.parser").find())
    test_manager.html_puller_chrome= html_puller_firefox
    assert test_manager.html_puller_chrome.html_source != "<html></html>" 

'''
The following consists of combinations of extensions.
'''

@when('we view the Firefox page with some canvas and font values interference')
def we_view_the_firefox_page_with_some_canvas_and_font_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["canvas", "font"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some canvas and screen values interference')
def we_view_the_firefox_page_with_some_canvas_and_screen_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["canvas", "screen"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 


@when('we view the Firefox page with some canvas and font and screen values interference')
def we_view_the_firefox_page_with_some_canvas_and_font_and_screen_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["canvas", "font", "screen"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some battery and clientRects and screen and webRTC values interference')
def we_view_the_firefox_page_with_some_battery_and_clientRects_and_screen_and_webRTC_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["battery", "clientRects", "screen",  "webRTC"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some battery and clientRects and navigator values interference')
def we_view_the_firefox_page_with_some_battery_and_clientRects_and_navigator_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["battery", "clientRects", "navigator"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some battery and clientRects and screen values interference')
def we_view_the_firefox_page_with_some_battery_and_clientRects_and_screen_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["battery", "clientRects", "screen"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some battery and clientRects and webgl values interference')
def we_view_the_firefox_page_with_some_battery_and_clientRects_and_webgl_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["battery", "clientRects", "webgl"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some battery and clientRects and webRTC values interference')
def we_view_the_firefox_page_with_some_battery_and_clientRects_and_webRTC_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["battery", "clientRects", "webRTC"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some battery and clientRects and navigator and webgl values interference')
def we_view_the_firefox_page_with_some_battery_and_clientRects_and_navigator_and_webgl_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["battery", "clientRects", "navigator",  "webgl"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some battery and clientRects and navigator and webRTC values interference')
def we_view_the_firefox_page_with_some_battery_and_clientRects_and_navigator_and_webRTC_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["battery", "clientRects", "navigator",  "webRTC"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and navigator and screen and webRTC values interference')
def we_view_the_firefox_page_with_some_audio_and_navigator_and_screen_and_webRTC_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "navigator", "screen",  "webRTC"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and navigator and webgl values interference')
def we_view_the_firefox_page_with_some_audio_and_navigator_and_webgl_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "navigator", "webgl"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and navigator and webRTC values interference')
def we_view_the_firefox_page_with_some_audio_and_navigator_and_webRTC_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "navigator", "webRTC"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and font and screen and webRTC values interference')
def we_view_the_firefox_page_with_some_audio_and_font_and_screen_and_webRTC_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "font", "screen",  "webRTC"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and font and screen values interference')
def we_view_the_firefox_page_with_some_audio_and_font_and_screen_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "font", "screen"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and font and webgl values interference')
def we_view_the_firefox_page_with_some_audio_and_font_and_webgl_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "font", "webgl"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and font and webRTC values interference')
def we_view_the_firefox_page_with_some_audio_and_font_and_webRTC_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "font", "webRTC"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and font and navigator and webgl values interference')
def we_view_the_firefox_page_with_some_audio_and_font_and_navigator_and_webgl_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "font", "navigator",  "webgl"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and font and navigator and webRTC values interference')
def we_view_the_firefox_page_with_some_audio_and_font_and_navigator_and_webRTC_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "font", "navigator",  "webRTC"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and clientRects and screen and webRTC values interference')
def we_view_the_firefox_page_with_some_audio_and_clientRects_and_screen_and_webRTC_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "clientRects", "screen",  "webRTC"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and clientRects and navigator values interference')
def we_view_the_firefox_page_with_some_audio_and_clientRects_and_navigator_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "clientRects", "navigator"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and clientRects and screen values interference')
def we_view_the_firefox_page_with_some_audio_and_clientRects_and_screen_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "clientRects", "screen"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and clientRects and webgl values interference')
def we_view_the_firefox_page_with_some_audio_and_clientRects_and_webgl_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "clientRects", "webgl"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and clientRects and webRTC values interference')
def we_view_the_firefox_page_with_some_audio_and_clientRects_and_webRTC_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "clientRects", "webRTC"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and clientRects and navigator and webgl values interference')
def we_view_the_firefox_page_with_some_audio_and_clientRects_and_navigator_and_webgl_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "clientRects", "navigator",  "webgl"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and clientRects and navigator and webRTC values interference')
def we_view_the_firefox_page_with_some_audio_and_clientRects_and_navigator_and_webRTC_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "clientRects", "navigator",  "webRTC"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and clientRects and font and screen values interference')
def we_view_the_firefox_page_with_some_audio_and_clientRects_and_font_and_screen_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "clientRects", "font",  "screen"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@when('we view the Firefox page with some audio and clientRects and font and webgl values interference')
def we_view_the_firefox_page_with_some_audio_and_clientRects_and_font_and_webgl_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "clientRects", "font",  "webgl"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@when('we view the Firefox page with some audio and clientRects and font and webRTC values interference')
def we_view_the_firefox_page_with_some_audio_and_clientRects_and_font_and_webRTC_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "clientRects", "font",  "webRTC"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@when('we view the Firefox page with some audio and canvas and screen values interference')
def we_view_the_firefox_page_with_some_audio_and_canvas_and_screen_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "canvas", "screen"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and canvas and webgl values interference')
def we_view_the_firefox_page_with_some_audio_and_canvas_and_webgl_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "canvas", "webgl"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and canvas and webRTC values interference')
def we_view_the_firefox_page_with_some_audio_and_canvas_and_webRTC_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "canvas", "webRTC"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and battery and navigator values interference')
def we_view_the_firefox_page_with_some_audio_and_battery_and_navigator_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "battery", "navigator"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and battery and screen values interference')
def we_view_the_firefox_page_with_some_audio_and_battery_and_screen_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "battery", "screen"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and battery and webgl values interference')
def we_view_the_firefox_page_with_some_audio_and_battery_and_webgl_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "battery", "webgl"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and battery and webRTC values interference')
def we_view_the_firefox_page_with_some_audio_and_battery_and_webRTC_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "battery", "webRTC"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 