from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('the Firefox audio and battery and screen value is saved')
def the_firefox_audio_and_battery_and_screen_value_is_saved(context):
    test_manager.html_puller_firefox.save_audio_value()
    test_manager.html_puller_chrome.save_battery_value() #TODO: See if this can be extracted from FingerprintJS
    assert test_manager.html_puller_firefox.save_screen_resolution_value()