from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *

test_manager = TestManager()
canvas_increment = 0

'''
The following definitions relate to the Firefox browser.
'''

@when('we view the Firefox page with some canvas and battery values interference')
def we_view_the_firefox_page_with_some_canvas_and_battery_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["canvas", "canvas"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some canvas and audio values interference')
def we_view_the_firefox_page_with_some_canvas_and_audio_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["canvas", "canvas"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some canvas and clientRects values interference')
def we_view_the_firefox_page_with_some_canvas_and_clientRects_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["canvas", "clientRects"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some canvas and font values interference')
# def we_view_the_firefox_page_with_some_canvas_and_font_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["canvas", "font"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some canvas and navigator values interference')
def we_view_the_firefox_page_with_some_canvas_and_navigator_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["canvas", "navigator"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some canvas and screen values interference')
# def we_view_the_firefox_page_with_some_canvas_and_screen_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["canvas", "screen"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some canvas and webgl values interference')
def we_view_the_firefox_page_with_some_canvas_and_webgl_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["canvas", "webgl"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some canvas and webRTC values interference')
def we_view_the_firefox_page_with_some_canvas_and_webRTC_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["canvas", "webRTC"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@then('we have a Firefox page which ran the canvas and battery response')
@then('we have a Firefox page which ran the canvas and audio response')
@then('we have a Firefox page which ran the canvas and clientRects response')
# @then('we have a Firefox page which ran the canvas and font response')
@then('we have a Firefox page which ran the canvas and navigator response')
@then('we have a Firefox page which ran the canvas and webgl response')
@then('we have a Firefox page which ran the canvas and webRTC response')
def we_have_a_firefox_page_which_ran_the_canvas_and_other_features_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

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

@then('the visitor id for canvas and battery is saved')
@then('the visitor id for canvas and audio is saved')
@then('the visitor id for canvas and clientRects is saved')
@then('the visitor id for canvas and navigator is saved')
@then('the visitor id for canvas and screen is saved')
@then('the visitor id for canvas and webgl is saved')
@then('the visitor id for canvas and webRTC is saved')
def the_firefox_visitor_id_for_canvas_and_other_features_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()