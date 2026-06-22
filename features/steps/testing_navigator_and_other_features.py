from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *

test_manager = TestManager()
navigator_increment = 0

'''
The following definitions relate to the Firefox browser.
'''

# @when('we view the Firefox page with some navigator and battery values interference')
# def we_view_the_firefox_page_with_some_navigator_and_battery_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["navigator", "battery"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some navigator and audio values interference')
# def we_view_the_firefox_page_with_some_navigator_and_audio_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["navigator", "audio"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some navigator and canvas values interference')
# def we_view_the_firefox_page_with_some_navigator_and_canvas_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["navigator", "canvas"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some navigator and clientRect values interference')
# def we_view_the_firefox_page_with_some_navigator_and_clientRects_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["navigator", "clientRect"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some navigator and font values interference')
# def we_view_the_firefox_page_with_some_navigator_and_font_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["navigator", "font"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some navigator and screen values interference')
# def we_view_the_firefox_page_with_some_navigator_and_screen_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["navigator", "screen"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some navigator and webgl values interference')
# def we_view_the_firefox_page_with_some_navigator_and_webgl_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["navigator", "webgl"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some navigator and webRTC values interference')
# def we_view_the_firefox_page_with_some_navigator_and_webRTC_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["navigator", "webRTC"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@then('we have a Firefox page which ran the navigator and battery response')
@then('we have a Firefox page which ran the navigator and audio response')
@then('we have a Firefox page which ran the navigator and canvas response')
@then('we have a Firefox page which ran the navigator and clientRect response')
@then('we have a Firefox page which ran the navigator and font response')
@then('we have a Firefox page which ran the navigator and screen response')
@then('we have a Firefox page which ran the navigator and webgl response')
@then('we have a Firefox page which ran the navigator and webRTC response')
def we_have_a_firefox_page_which_ran_the_navigator_and_other_features_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

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

@then('the visitor id for navigator and battery is saved')
@then('the visitor id for navigator and audio is saved')
@then('the visitor id for navigator and canvas is saved')
@then('the visitor id for navigator and clientRect is saved')
@then('the visitor id for navigator and font is saved')
@then('the visitor id for navigator and screen is saved')
@then('the visitor id for navigator and webgl is saved')
@then('the visitor id for navigator and webRTC is saved')
def the_firefox_visitor_id_for_navigator_and_other_features_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()