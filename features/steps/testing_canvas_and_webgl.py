from behave import *
from bs4 import BeautifulSoup
from ScrapeHTML.test_manager import *

test_manager = TestManager()
canvas_increment = 0

'''
The following definitions relate to the Firefox browser.
'''

@when('we view the Firefox page with no canvas or webgl values interference')
def we_view_the_firefox_page_with_no_canvas_or_webgl_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page(), "html.parser").find())
    test_manager.html_puller_firefox= html_puller_firefox
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@then('we have a Firefox page which ran the canvas and webgl response')
def we_have_a_firefox_page_which_ran_the_canvas_response(context):
    assert test_manager.html_puller_firefox.html_source != "<html></html>"

@when('we view the Firefox page with some canvas and webgl values interference')
def we_view_the_firefox_page_with_some_canvas_and_webgl_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension(["canvas", "webgl"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@then('the visitor id for canvas and webgl is saved')
def the_firefox_visitor_id_for_canvas_and_webgl_has_been_recorded(context):
    assert test_manager.html_puller_firefox.save_visitor_id_value()

@then('we will log the canvas and webgl testing time in the saved file')
def we_will_log_the_canvas_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("canvas and webgl")