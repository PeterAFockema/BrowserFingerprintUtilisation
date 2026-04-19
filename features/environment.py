from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

""" 
The code within the following block is checked before all/any of test steps are run.
This would be a great place to instantiate any of your class objects and store them as
attributes in behave's context object for later use.
"""
def before_scenario(self, context):         
    # The following creates an api_calls attribute for behave's context object
    # context.api_calls = ApiClient(context.config.userdata['url'])
    # test_manager.html_puller_firefox
    print("In environment.py initialising TestManager...")
    test_manager = TestManager()
    print("After initialising TestManager...")