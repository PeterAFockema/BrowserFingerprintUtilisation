from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *

test_manager = TestManager()
canvas_increment = 0

'''
The following definitions relate to the Firefox browser.
'''

@when('we view the Firefox page with no canvas or screen values interference')
def we_view_the_firefox_page_with_no_canvas_or_screen_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page(), "html.parser").find())
    test_manager.html_puller_firefox= html_puller_firefox
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we have a Firefox page which ran the canvas and screen response')
def we_have_a_firefox_page_which_ran_the_canvas_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@when('we view the Firefox page with some canvas and screen values interference')
def we_view_the_firefox_page_with_some_canvas_and_screen_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["canvas", "screen"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 