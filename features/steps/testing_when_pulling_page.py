# from behave import *
# from bs4 import BeautifulSoup

# from parse_type import TypeBuilder

# from ScrapeHTML.test_manager import *
# from ScrapeHTML.defined_values import *

# # Create a comma-separated string-list parser function
# parse_extension_list = TypeBuilder.with_many(lambda text: text.strip(), listsep=",")

# # Register the converter with Behave mapping "List" to your new parser function
# register_type(List=parse_extension_list)

# '''
# The following consists of combinations of extensions and single extensions.
# This single, consolidated step fully replaces all individual string-matching steps.
# '''

# @when("we view the Firefox page with some {extension_list:List} values interference")
# def we_view_the_firefox_page_with_some_interference(context, extension_list):
#     """
#     Consolidated step to handle single features or any combination of parameters.
#     Example steps in feature file:
#       When we view the Firefox page with some audio values interference
#       When we view the Firefox page with some canvas, font values interference
#     """
#     html_puller_firefox = test_manager.html_puller_firefox
    
#     # Check if we are running a single special extension that uses a distinct method
#     if len(extension_list) == 1 and extension_list[0] == "canvas":
#         html_content = html_puller_firefox.pull_HTML_page_with_canvas_extension()
#     elif len(extension_list) == 1:
#         html_content = html_puller_firefox.pull_HTML_page_with_extension_string(extension_list[0])
#     else:
#         html_content = html_puller_firefox.pull_HTML_page_with_extension_list(extension_list)
    
#     # Store source securely in the context object to isolate state
#     context.html_source = html_content
    
#     # Clean assertions without mutating global variables
#     assert context.html_source != "<html></html>", "HTML source was empty <html></html>"
#     soup = BeautifulSoup(html_content, "html.parser")
#     assert soup.find() is not None, "Parsed HTML was empty or returned None"