from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('we will log the no parameter and buffer testing time in the saved file')
def we_will_log_the_no_parameter_and_buffer_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("no parameter and buffer")

@then('we will log the parameter testing time in the saved file')
def we_will_log_the_parameter_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("parameter")

@then('we will log the buffer testing time in the saved file')
def we_will_log_the_buffer_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("buffer")

@then('we will log the parameter and buffer values testing time in the saved file')
def we_will_log_the_parameter_and_buffer_values_testing_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("parameter and buffer")