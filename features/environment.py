from ScrapeHTML.test_manager import *
from ScrapeHTML.defined_values import *

from shiftingbrowserfingerprints.generate_xpis import build_all_unsigned_xpi_extensions


""" 
The code within the following block is checked before all/any of test steps are run.
This would be a great place to instantiate any of your class objects and store them as
attributes in behave's context object for later use.
"""
def before_scenario(self, context):         
    print("In environment.py. Initialising TestManager...")
    test_manager = TestManager()
    print("After initialising TestManager...")

def before_feature(context, feature):
    print(f"In environment.py. We Are Starting Feature: {feature.name}")
    build_all_unsigned_xpi_extensions()
