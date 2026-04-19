from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *

test_manager = TestManager()
battery_and_canvas_and_font_increment = 0

'''
The following definitions relate to the Firefox browser.
'''

@when('we view the Firefox page with some battery and canvas and font and navigator values interference')
def we_view_the_firefox_page_with_some_battery_and_canvas_and_font_and_navigator_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["battery", "canvas", "font",  "navigator"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some battery and canvas and font and screen values interference')
def we_view_the_firefox_page_with_some_battery_and_canvas_and_font_and_screen_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["battery", "canvas", "font",  "screen"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some battery and canvas and font and webgl values interference')
def we_view_the_firefox_page_with_some_battery_and_canvas_and_font_and_webgl_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["battery", "canvas", "font",  "webgl"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some battery and canvas and font and webRTC values interference')
def we_view_the_firefox_page_with_some_battery_and_canvas_and_font_and_webRTC_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["battery", "canvas", "font",  "webRTC"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@then('we have a Firefox page which ran the battery and canvas and font and navigator response')
@then('we have a Firefox page which ran the battery and canvas and font and screen response')
@then('we have a Firefox page which ran the battery and canvas and font and webgl response')
@then('we have a Firefox page which ran the battery and canvas and font and webRTC response')
def we_have_a_firefox_page_which_ran_the_battery_and_canvas_and_font_and_other_features_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we will log the battery and canvas and font and navigator testing time in the saved file')
def we_will_log_the_battery_and_canvas_and_font_navigator_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and canvas and font and navigator")

@then('we will log the battery and canvas and font and screen testing time in the saved file')
def we_will_log_the_battery_and_canvas_and_font_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and canvas and font and screen")

@then('we will log the battery and canvas and font and webgl testing time in the saved file')
def we_will_log_the_battery_and_canvas_and_font_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and canvas and font and webgl")

@then('we will log the battery and canvas and font and webRTC testing time in the saved file')
def we_will_log_the_battery_and_canvas_and_font_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and canvas and font and webRTC")

@then('the visitor id for battery and canvas and font and navigator is saved')
@then('the visitor id for battery and canvas and font and screen is saved')
@then('the visitor id for battery and canvas and font and webgl is saved')
@then('the visitor id for battery and canvas and font and webRTC is saved')
def the_firefox_visitor_id_for_battery_and_canvas_and_font_and_other_features_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()
