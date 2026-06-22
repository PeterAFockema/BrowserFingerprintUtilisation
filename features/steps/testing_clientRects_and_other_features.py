from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *

test_manager = TestManager()
clientRects_increment = 0

'''
The following definitions relate to the Firefox browser.
'''

# @when('we view the Firefox page with some clientRects and battery values interference')
# def we_view_the_firefox_page_with_some_clientRects_and_battery_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["clientRects", "clientRects"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some clientRects and audio values interference')
# def we_view_the_firefox_page_with_some_clientRects_and_audio_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["clientRects", "clientRects"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some clientRects and canvas values interference')
# def we_view_the_firefox_page_with_some_clientRects_and_canvas_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["clientRects", "clientRects"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some clientRects and font values interference')
# def we_view_the_firefox_page_with_some_clientRects_and_font_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["clientRects", "font"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some clientRects and navigator values interference')
# def we_view_the_firefox_page_with_some_clientRects_and_navigator_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["clientRects", "navigator"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some clientRects and screen values interference')
# def we_view_the_firefox_page_with_some_clientRects_and_screen_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["clientRects", "screen"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some clientRects and webgl values interference')
# def we_view_the_firefox_page_with_some_clientRects_and_webgl_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["clientRects", "webgl"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

# @when('we view the Firefox page with some clientRects and webRTC values interference')
# def we_view_the_firefox_page_with_some_clientRects_and_webRTC_values_interference(context):
#     html_puller_firefox = test_manager.html_puller_firefox
#     bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["clientRects", "webRTC"]), "html.parser").find())
#     assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@then('we have a Firefox page which ran the clientRects and battery response')
@then('we have a Firefox page which ran the clientRects and audio response')
@then('we have a Firefox page which ran the clientRects and canvas response')
@then('we have a Firefox page which ran the clientRects and font response')
@then('we have a Firefox page which ran the clientRects and navigator response')
@then('we have a Firefox page which ran the clientRects and screen response')
@then('we have a Firefox page which ran the clientRects and webgl response')
@then('we have a Firefox page which ran the clientRects and webRTC response')
def we_have_a_firefox_page_which_ran_the_clientRects_and_other_features_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we will log the clientRects and battery testing time in the saved file')
def we_will_log_the_clientRects_and_battery_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and battery")

@then('we will log the clientRects and audio testing time in the saved file')
def we_will_log_the_clientRects_and_audio_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and audio")

@then('we will log the clientRects and canvas testing time in the saved file')
def we_will_log_the_clientRects_and_canvas_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and canvas")

@then('we will log the clientRects and font testing time in the saved file')
def we_will_log_the_clientRects_and_font_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and font")

@then('we will log the clientRects and navigator testing time in the saved file')
def we_will_log_the_clientRects_and_navigator_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and navigator")

@then('we will log the clientRects and screen testing time in the saved file')
def we_will_log_the_clientRects_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and screen")

@then('we will log the clientRects and webgl testing time in the saved file')
def we_will_log_the_clientRects_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and webgl")

@then('we will log the clientRects and webRTC testing time in the saved file')
def we_will_log_the_clientRects_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("clientRects and webRTC")

@then('the visitor id for clientRects and battery is saved')
@then('the visitor id for clientRects and audio is saved')
@then('the visitor id for clientRects and canvas is saved')
@then('the visitor id for clientRects and font is saved')
@then('the visitor id for clientRects and navigator is saved')
@then('the visitor id for clientRects and screen is saved')
@then('the visitor id for clientRects and webgl is saved')
@then('the visitor id for clientRects and webRTC is saved')
def the_firefox_visitor_id_for_clientRects_and_other_features_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()