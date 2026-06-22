from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('we have a Firefox page which ran the battery and clientRects and font and webgl and webgl response')
@then('we have a Firefox page which ran the battery and clientRects and font and webgl and webRTC response')
def we_have_a_firefox_page_which_ran_the_battery_and_clientRects_and_font_and_other_features_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we will log the battery and clientRects and font and webgl and webRTC testing time in the saved file')
def we_will_log_the_battery_and_clientRects_and_font_and_webgl_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and clientRects and font and webgl and webRTC")

@then('the visitor id for battery and clientRects and font and webgl and webRTC is saved')
def the_firefox_visitor_id_for_battery_and_clientRects_and_font_and_webgl_and_other_features_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()
