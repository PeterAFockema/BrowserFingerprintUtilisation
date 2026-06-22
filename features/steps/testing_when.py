import re

from behave import *
from bs4 import BeautifulSoup

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

use_step_matcher("cfparse")

def execute_firefox_scrape(extensions):
    """Helper utility to process the browser extensions list and run assertions."""
    html_puller_firefox = test_manager.html_puller_firefox
    html_content = html_puller_firefox.pull_HTML_page_with_extension_list(extensions)
    
    soup = BeautifulSoup(html_content, "html.parser")
    bool(soup.find())
    
    assert test_manager.html_puller_firefox.html_source != "<html></html>"


@when('we view the Firefox page with some {prefix_extensions} and {last_item:w} values interference')
def we_view_the_firefox_page_with_mixed_interferences(context, prefix_extensions, last_item):
    # This step handles complex combinations like: "audio and battery and canvas and {last_item}"
    extensions = re.findall(r'\b\w+\b', prefix_extensions)
    exclusions = {"and", "some"}
    cleaned_extensions = [item for item in extensions if item not in exclusions]
    
    cleaned_extensions.append(last_item)
    execute_firefox_scrape(cleaned_extensions)


@when('we view the Firefox page with some {extension_string} values interference')
def we_view_the_firefox_page_with_any_interferences(context, extension_string):
    # This step handles flatter single-phrase combinations like: "audio and battery and canvas"
    extensions = re.findall(r'\b\b\w+\b', extension_string)
    exclusions = {"and", "some", "values", "interference"}
    cleaned_extensions = [item for item in extensions if item not in exclusions]
    
    execute_firefox_scrape(cleaned_extensions)