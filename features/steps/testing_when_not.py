from behave import *
from bs4 import BeautifulSoup

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@when('we view the Firefox page with no canvas or screen values interference')
@when('we view the Firefox page with no toBlob and toDataURL values interference')
@when('we view the Firefox page with no offsetHeight and offsetWidth values interference')
@when('we view the Firefox page with no navigator values interference')
@when('we view the Firefox page with no audio values interference')
@when('we view the Firefox page with no battery values interference')
@when('we view the Firefox page with no canvas or webgl values interference')
@when('we view the Firefox page with no clientRects values interference')
@when('we view the Firefox page with no font values interference')
@when('we view the Firefox page with no canvas values interference')
@when('we view the Firefox page with no availHeight or availWidth or colorDepth values interference')
@when('we view the Firefox page with no screen values interference')
@when('we view the Firefox page with no parameter or buffer values interference')
@when('we view the Firefox page with no webgl values interference')
@when('we view the Firefox page with no webRTC values interference')
@when('we view the Firefox page with no canvas or font or screen values interference')
def we_view_the_firefox_page_with_no_canvas_or_font_or_screen_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page(), "html.parser").find())
    test_manager.html_puller_firefox= html_puller_firefox
    assert test_manager.html_puller_firefox.html_source != "<html></html>"