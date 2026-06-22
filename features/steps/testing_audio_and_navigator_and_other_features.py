from behave import *
from bs4 import BeautifulSoup

from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

'''
The following definitions relate to the Firefox browser.
'''

@when('we view the Firefox page with some audio and navigator and webgl values interference')
def we_view_the_firefox_page_with_some_audio_and_navigator_and_webgl_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "navigator", "webgl"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@when('we view the Firefox page with some audio and navigator and webRTC values interference')
def we_view_the_firefox_page_with_some_audio_and_navigator_and_webRTC_values_interference(context):
    html_puller_firefox = test_manager.html_puller_firefox
    bool(BeautifulSoup(html_puller_firefox.pull_HTML_page_with_extension_list(["audio", "navigator", "webRTC"]), "html.parser").find())
    assert test_manager.html_puller_firefox.html_source != "<html></html>" 

@then('we will log the audio and navigator and screen testing time in the saved file')
def we_will_log_the_audio_and_navigator_and_screen_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and navigator and screen")

@then('we will log the audio and navigator and webgl testing time in the saved file')
def we_will_log_the_audio_and_navigator_and_webgl_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and navigator and webgl")

@then('we will log the audio and navigator and webRTC testing time in the saved file')
def we_will_log_the_audio_and_navigator_and_webRTC_time_in_the_saved_file(context):
    assert test_manager.html_puller_firefox.log_time_in_save_file("audio and navigator and webRTC")
   