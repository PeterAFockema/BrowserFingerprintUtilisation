from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

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