from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

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