from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *

test_manager = TestManager()
battery_increment = 0

'''
The following definitions relate to the Firefox browser.
'''

# @when('we view the Firefox page with some battery and audio values interference')
# def we_view_the_firefox_page_with_some_battery_and_audio_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["battery", "audio"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some battery and canvas values interference')
# def we_view_the_firefox_page_with_some_battery_and_canvas_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["battery", "canvas"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some battery and clientRects values interference')
# def we_view_the_firefox_page_with_some_battery_and_clientRects_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["battery", "clientRects"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some battery and font values interference')
# def we_view_the_firefox_page_with_some_battery_and_font_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["battery", "font"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some battery and navigator values interference')
# def we_view_the_firefox_page_with_some_battery_and_navigator_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["battery", "navigator"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some battery and screen values interference')
# def we_view_the_firefox_page_with_some_battery_and_screen_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["battery", "screen"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some battery and webgl values interference')
# def we_view_the_firefox_page_with_some_battery_and_webgl_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["battery", "webgl"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some battery and webRTC values interference')
# def we_view_the_firefox_page_with_some_battery_and_webRTC_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["battery", "webRTC"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@then('we have a Firefox page which ran the battery and audio response')
@then('we have a Firefox page which ran the battery and canvas response')
@then('we have a Firefox page which ran the battery and clientRects response')
@then('we have a Firefox page which ran the battery and font response')
@then('we have a Firefox page which ran the battery and navigator response')
@then('we have a Firefox page which ran the battery and screen response')
@then('we have a Firefox page which ran the battery and webgl response')
@then('we have a Firefox page which ran the battery and webRTC response')
def we_have_a_firefox_page_which_ran_the_battery_and_other_features_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

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

@then('the visitor id for battery and audio is saved')
@then('the visitor id for battery and canvas is saved')
@then('the visitor id for battery and clientRects is saved')
@then('the visitor id for battery and font is saved')
@then('the visitor id for battery and navigator is saved')
@then('the visitor id for battery and screen is saved')
@then('the visitor id for battery and webgl is saved')
@then('the visitor id for battery and webRTC is saved')
def the_firefox_visitor_id_for_battery_and_other_features_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()
