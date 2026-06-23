from behave import *

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *
'''
The following definitions relate to the Firefox browser.
'''

@then('the Firefox webgl value is saved')
def the_firefox_webgl_value_has_been_recorded(context):
    test_manager.html_puller_firefox.save_web_gl_value()
