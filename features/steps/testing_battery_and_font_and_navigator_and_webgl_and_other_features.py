from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('we have a Firefox page which ran the battery and font and navigator and webgl and webgl response')
@then('we have a Firefox page which ran the battery and font and navigator and webgl and webRTC response')
def we_have_a_firefox_page_which_ran_the_battery_and_font_and_navigator_and_other_features_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we will log the battery and font and navigator and webgl and webRTC testing time in the saved file')
def we_will_log_the_battery_and_font_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("battery and font and navigator and webgl and webRTC")
