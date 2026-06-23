from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
Dynamically logs testing times for Firefox based on the feature file step.
Example: "audio and battery and canvas and clientRects and font"
'''

@then('we will log the {test_combination} testing time in the saved file') 
def we_will_log_testing_time_in_the_saved_file(context, test_combination):
    assert test_manager.html_puller_firefox.log_time_in_save_file(test_combination)
