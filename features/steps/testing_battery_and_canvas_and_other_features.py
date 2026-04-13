from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *

test_manager = TestManager()
battery and canvas_increment = 0

'''
The following definitions relate to the Firefox browser.
'''

@when('we view the Firefox page with some battery and canvas and clientRects values interference')
def we_view_the_firefox_page_with_some_battery_and_canvas_and_clientRects_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["battery", "canvas", "clientRects"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some battery and canvas and font values interference')
def we_view_the_firefox_page_with_some_battery_and_canvas_and_font_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["battery", "canvas", "font"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some battery and canvas and navigator values interference')
def we_view_the_firefox_page_with_some_battery_and_canvas_and_navigator_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["battery", "canvas", "navigator"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some battery and canvas and screen values interference')
def we_view_the_firefox_page_with_some_battery_and_canvas_and_screen_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["battery", "canvas", "screen"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some battery and canvas and webgl values interference')
def we_view_the_firefox_page_with_some_battery_and_canvas_and_webgl_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["battery", "canvas", "webgl"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some battery and canvas and webRTC values interference')
def we_view_the_firefox_page_with_some_battery_and_canvas_and_webRTC_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["battery", "canvas", "webRTC"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@then('we have a Firefox page which ran the battery and canvas and clientRects response')
@then('we have a Firefox page which ran the battery and canvas and font response')
@then('we have a Firefox page which ran the battery and canvas and navigator response')
@then('we have a Firefox page which ran the battery and canvas and screen response')
@then('we have a Firefox page which ran the battery and canvas and webgl response')
@then('we have a Firefox page which ran the battery and canvas and webRTC response')
def we_have_a_firefox_page_which_ran_the_battery_and_canvas_and_other_features_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we will log the battery and canvas and clientRects testing time in the saved file')
def we_will_log_the_battery_and_canvas_and_clientRects_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and canvas and clientRects")

@then('we will log the battery and canvas and font testing time in the saved file')
def we_will_log_the_battery_and_canvas_and_font_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and canvas and font")

@then('we will log the battery and canvas and navigator testing time in the saved file')
def we_will_log_the_battery_and_canvas_and_navigator_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and canvas and navigator")

@then('we will log the battery and canvas and screen testing time in the saved file')
def we_will_log_the_battery_and_canvas_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and canvas and screen")

@then('we will log the battery and canvas and webgl testing time in the saved file')
def we_will_log_the_battery_and_canvas_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and canvas and webgl")

@then('we will log the battery_and_canvas and webRTC testing time in the saved file')
def we_will_log_the_battery_and_canvas_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and canvas and webRTC")

@then('the visitor id for battery and canvas and canvas is saved')
@then('the visitor id for battery and canvas and clientRects is saved')
@then('the visitor id for battery and canvas and font is saved')
@then('the visitor id for battery and canvas and navigator is saved')
@then('the visitor id for battery and canvas and screen is saved')
@then('the visitor id for battery and canvas and webgl is saved')
@then('the visitor id for battery and canvas and webRTC is saved')
def the_firefox_visitor_id_for_battery_and_canvas_and_other_features_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()
