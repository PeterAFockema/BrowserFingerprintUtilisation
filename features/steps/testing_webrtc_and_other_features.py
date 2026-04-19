from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *

test_manager = TestManager()
webrtc_increment = 0

'''
The following definitions relate to the Firefox browser.
'''

@when('we view the Firefox page with some webrtc and battery values interference')
def we_view_the_firefox_page_with_some_webrtc_and_battery_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["webrtc", "battery"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some webrtc and audio values interference')
def we_view_the_firefox_page_with_some_webrtc_and_audio_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["webrtc", "audio"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some webrtc and canvas values interference')
def we_view_the_firefox_page_with_some_webrtc_and_canvas_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["webrtc", "canvas"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some webrtc and clientRect values interference')
def we_view_the_firefox_page_with_some_webrtc_and_clientRects_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["webrtc", "clientRect"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some webrtc and font values interference')
def we_view_the_firefox_page_with_some_webrtc_and_font_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["webrtc", "font"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some webrtc and navigator values interference')
def we_view_the_firefox_page_with_some_webrtc_and_navigator_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["webrtc", "navigator"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some webrtc and screen values interference')
def we_view_the_firefox_page_with_some_webrtc_and_screen_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["webrtc", "screen"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some webrtc and webgl values interference')
def we_view_the_firefox_page_with_some_webrtc_and_webgl_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["webrtc", "webgl"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@then('we have a Firefox page which ran the webrtc and battery response')
@then('we have a Firefox page which ran the webrtc and audio response')
@then('we have a Firefox page which ran the webrtc and canvas response')
@then('we have a Firefox page which ran the webrtc and clientRect response')
@then('we have a Firefox page which ran the webrtc and font response')
@then('we have a Firefox page which ran the webrtc and navigator response')
@then('we have a Firefox page which ran the webrtc and screen response')
@then('we have a Firefox page which ran the webrtc and webgl response')
def we_have_a_firefox_page_which_ran_the_webrtc_and_other_features_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

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

@then('the visitor id for webrtc and battery is saved')
@then('the visitor id for webrtc and audio is saved')
@then('the visitor id for webrtc and canvas is saved')
@then('the visitor id for webrtc and clientRect is saved')
@then('the visitor id for webrtc and font is saved')
@then('the visitor id for webrtc and navigator is saved')
@then('the visitor id for webrtc and screen is saved')
@then('the visitor id for webrtc and webgl is saved')
def the_firefox_visitor_id_for_webrtc_and_other_features_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()