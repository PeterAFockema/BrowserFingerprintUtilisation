from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('we have a Firefox page which ran the screen and battery response')
@then('we have a Firefox page which ran the screen and audio response')
@then('we have a Firefox page which ran the screen and canvas response')
@then('we have a Firefox page which ran the screen and clientRect response')
@then('we have a Firefox page which ran the screen and font response')
@then('we have a Firefox page which ran the screen and navigator response')
@then('we have a Firefox page which ran the screen and webgl response')
@then('we have a Firefox page which ran the screen and webRTC response')
def we_have_a_firefox_page_which_ran_the_screen_and_other_features_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we will log the screen and battery testing time in the saved file')
def we_will_log_the_screen_and_battery_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("screen and battery")

@then('we will log the screen and audio testing time in the saved file')
def we_will_log_the_screen_and_audio_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("screen and audio")

@then('we will log the screen and canvas testing time in the saved file')
def we_will_log_the_screen_and_canvas_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("screen and canvas")

@then('we will log the screen and clientRect testing time in the saved file')
def we_will_log_the_screen_and_clientRect_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("screen and clientRect")

@then('we will log the screen and font testing time in the saved file')
def we_will_log_the_screen_and_font_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("screen and font")

@then('we will log the screen and navigator testing time in the saved file')
def we_will_log_the_screen_and_navigator_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("screen and navigator")

@then('we will log the screen and webgl testing time in the saved file')
def we_will_log_the_screen_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("screen and webgl")

@then('we will log the screen and webRTC testing time in the saved file')
def we_will_log_the_screen_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("screen and webRTC")

@then('the visitor id for screen and battery is saved')
@then('the visitor id for screen and audio is saved')
@then('the visitor id for screen and canvas is saved')
@then('the visitor id for screen and clientRect is saved')
@then('the visitor id for screen and font is saved')
@then('the visitor id for screen and navigator is saved')
@then('the visitor id for screen and webgl is saved')
@then('the visitor id for screen and webRTC is saved')
def the_firefox_visitor_id_for_screen_and_other_features_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()