from behave import *
from bs4 import BeautifulSoup

from parse_type import TypeBuilder

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser and only a single extension.
'''

@when('we view the Firefox page with some audio values interference')
def we_view_the_firefox_page_with_some_audio_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_string("audio"), "html.parser").find())
    test_manager.html_puller_chrome= html_puller_firefox
    assert test_manager.html_puller_chrome.html_source != "<html></html>" 

@when('we view the Firefox page with some battery values interference')
def we_view_the_firefox_page_with_some_battery_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_string("battery"), "html.parser").find())
    test_manager.html_puller_chrome= html_puller_firefox
    assert test_manager.html_puller_chrome.html_source != "<html></html>" 

@when('we view the Firefox page with some canvas values interference')
def we_view_the_firefox_page_with_some_canvas_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_canvas_extension(), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some clientRects values interference')
def we_view_the_firefox_page_with_some_clientRects_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_string("clientRects"), "html.parser").find())
    test_manager.html_puller_chrome= html_puller_firefox
    assert test_manager.html_puller_chrome.html_source != "<html></html>" 

@when('we view the Firefox page with some toBlob values interference')
def we_view_the_firefox_page_with_some_toBlob_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_string("toBlob"), "html.parser").find())
    test_manager.html_puller_chrome= html_puller_firefox
    assert test_manager.html_puller_chrome.html_source != "<html></html>" 

'''
The following consists of combinations of extensions.
'''

# Register a custom type to parse lists (e.g., "canvas, font, screen") directly in the step string
list_type = TypeBuilder.with_list(str)
register_type(list_type)

@when("we view the Firefox page with some {extension_list:List} values interference")
def we_view_the_firefox_page_with_some_interference(context, extension_list):
    """
    Consolidated step to handle any combination of feature/interference parameters.
    Example step in feature file:
      When we view the Firefox page with some canvas, font values interference
    """
    html_puller_firefox = test_manager.html_puller_firefox
    
    # Fetch the HTML page using the dynamically parsed list
    raw_html = html_puller_firefox.pull_HTML_page_with_extension_list(extension_list)
    
    # Assertions
    assert html_puller_firefox.html_source != "<html></html>", "HTML source was empty <html></html>"
    
    # Check if the BeautifulSoup parser successfully finds elements
    parsed_html = BeautifulSoup(raw_html, "html.parser").find()
    assert parsed_html is not None, "Parsed HTML was empty or returned None"