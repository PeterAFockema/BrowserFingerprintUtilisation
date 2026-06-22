from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *

test_manager = TestManager()
canvas_and_clientRects_and_font_and_navigator_increment = 0

'''
The following definitions relate to the Firefox browser.
'''

# @when('we view the Firefox page with some canvas and clientRects and font and navigator and screen values interference')
# def we_view_the_firefox_page_with_some_canvas_and_clientRects_and_font_and_screen_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["canvas", "clientRects", "font", "navigator", "screen"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some canvas and clientRects and font and navigator and webgl values interference')
# def we_view_the_firefox_page_with_some_canvas_and_clientRects_and_font_and_webgl_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["canvas", "clientRects", "font", "navigator",  "webgl"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some canvas and clientRects and font and navigator and webRTC values interference')
# def we_view_the_firefox_page_with_some_canvas_and_clientRects_and_font_and_webRTC_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["canvas", "clientRects", "font", "navigator", "webRTC"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@then('we have a Firefox page which ran the canvas and clientRects and font and navigator and screen response')
@then('we have a Firefox page which ran the canvas and clientRects and font and navigator and webgl response')
@then('we have a Firefox page which ran the canvas and clientRects and font and navigator and webRTC response')
def we_have_a_firefox_page_which_ran_the_canvas_and_clientRects_and_font_and_other_features_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we will log the canvas and clientRects and font and navigator and screen testing time in the saved file')
def we_will_log_the_canvas_and_clientRects_and_font_and_navigator_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and clientRects and font and navigator and screen")

@then('we will log the canvas and clientRects and font and navigator and webgl testing time in the saved file')
def we_will_log_the_canvas_and_clientRects_and_font_and_navigator_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and clientRects and font and navigator and webgl")

@then('we will log the canvas and clientRects and font and navigator and webRTC testing time in the saved file')
def we_will_log_the_canvas_and_clientRects_and_font_and_navigator_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and clientRects and font and navigator and webRTC")

@then('the visitor id for canvas and clientRects and font and navigator and screen is saved')
@then('the visitor id for canvas and clientRects and font and navigator and webgl is saved')
@then('the visitor id for canvas and clientRects and font and navigator and webRTC is saved')
def the_firefox_visitor_id_for_canvas_and_clientRects_and_font_and_navigator_and_other_features_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()
