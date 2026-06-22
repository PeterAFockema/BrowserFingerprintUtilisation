from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *

test_manager = TestManager()
webgl_increment = 0

'''
The following definitions relate to the Firefox browser.
'''

# @when('we view the Firefox page with some webgl and battery values interference')
# def we_view_the_firefox_page_with_some_webgl_and_battery_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["webgl", "battery"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some webgl and audio values interference')
# def we_view_the_firefox_page_with_some_webgl_and_audio_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["webgl", "audio"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some webgl and canvas values interference')
# def we_view_the_firefox_page_with_some_webgl_and_canvas_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["webgl", "canvas"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some webgl and clientRect values interference')
# def we_view_the_firefox_page_with_some_webgl_and_clientRects_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["webgl", "clientRect"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some webgl and font values interference')
# def we_view_the_firefox_page_with_some_webgl_and_font_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["webgl", "font"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some webgl and navigator values interference')
# def we_view_the_firefox_page_with_some_webgl_and_navigator_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["webgl", "navigator"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some webgl and screen values interference')
# def we_view_the_firefox_page_with_some_webgl_and_screen_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["webgl", "screen"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some webgl and webRTC values interference')
# def we_view_the_firefox_page_with_some_webgl_and_webRTC_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["webgl", "webRTC"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@then('we have a Firefox page which ran the webgl and battery response')
@then('we have a Firefox page which ran the webgl and audio response')
@then('we have a Firefox page which ran the webgl and canvas response')
@then('we have a Firefox page which ran the webgl and clientRect response')
@then('we have a Firefox page which ran the webgl and font response')
@then('we have a Firefox page which ran the webgl and navigator response')
@then('we have a Firefox page which ran the webgl and screen response')
@then('we have a Firefox page which ran the webgl and webRTC response')
def we_have_a_firefox_page_which_ran_the_webgl_and_other_features_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

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

@then('the visitor id for webgl and battery is saved')
@then('the visitor id for webgl and audio is saved')
@then('the visitor id for webgl and canvas is saved')
@then('the visitor id for webgl and clientRect is saved')
@then('the visitor id for webgl and font is saved')
@then('the visitor id for webgl and navigator is saved')
@then('the visitor id for webgl and screen is saved')
@then('the visitor id for webgl and webRTC is saved')
def the_firefox_visitor_id_for_webgl_and_other_features_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()