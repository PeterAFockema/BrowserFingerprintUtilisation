from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@then('we have a Firefox page which ran the canvas and font response')
def we_have_a_firefox_page_which_ran_the_canvas_and_font_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@when('we view the Firefox page with some canvas and font values interference')
def we_view_the_firefox_page_with_some_canvas_and_font_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["canvas", "font"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 
