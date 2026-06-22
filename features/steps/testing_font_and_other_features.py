from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *

test_manager = TestManager()
font_increment = 0

'''
The following definitions relate to the Firefox browser.
'''

# @when('we view the Firefox page with some font and battery values interference')
# def we_view_the_firefox_page_with_some_font_and_battery_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["font", "battery"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some font and audio values interference')
# def we_view_the_firefox_page_with_some_font_and_audio_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["font", "audio"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some font and canvas values interference')
# def we_view_the_firefox_page_with_some_font_and_canvas_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["font", "canvas"]), "html.parser").find())
    # assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some font and clientRect values interference')
# def we_view_the_firefox_page_with_some_font_and_clientRects_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["font", "clientRect"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some font and navigator values interference')
# def we_view_the_firefox_page_with_some_font_and_navigator_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["font", "navigator"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some font and screen values interference')
# def we_view_the_firefox_page_with_some_font_and_screen_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["font", "screen"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some font and webgl values interference')
# def we_view_the_firefox_page_with_some_font_and_webgl_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["font", "webgl"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some font and webRTC values interference')
# def we_view_the_firefox_page_with_some_font_and_webRTC_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["font", "webRTC"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@then('we have a Firefox page which ran the font and battery response')
@then('we have a Firefox page which ran the font and audio response')
@then('we have a Firefox page which ran the font and canvas response')
@then('we have a Firefox page which ran the font and clientRect response')
@then('we have a Firefox page which ran the font and navigator response')
@then('we have a Firefox page which ran the font and screen response')
@then('we have a Firefox page which ran the font and webgl response')
@then('we have a Firefox page which ran the font and webRTC response')
def we_have_a_firefox_page_which_ran_the_font_and_other_features_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

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

@then('the visitor id for font and battery is saved')
@then('the visitor id for font and audio is saved')
@then('the visitor id for font and canvas is saved')
@then('the visitor id for font and clientRect is saved')
@then('the visitor id for font and navigator is saved')
@then('the visitor id for font and screen is saved')
@then('the visitor id for font and webgl is saved')
@then('the visitor id for font and webRTC is saved')
def the_firefox_visitor_id_for_font_and_other_features_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()