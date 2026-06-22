from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('we will log the font and navigator and screen and webgl and webRTC testing time in the saved file')
def we_will_log_the_font_and_navigator_and_screen_and_webgl_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("font and navigator and screen and webgl and webRTC")
