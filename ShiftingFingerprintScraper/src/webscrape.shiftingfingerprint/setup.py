from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='webscrape.shiftingfingerprint',
      version=version,
      description="A web scraper that can utilise fingerprint obfuscation techniques.",
      long_description="""\
A web scraper that can utilise fingerprint obfuscation techniques against browser fingerprinting software.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Peter Fockema',
      author_email='',
      url='',
      license='Apache License Version 2.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
          'selenium',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
