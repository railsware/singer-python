#!/usr/bin/env python

from setuptools import setup, find_packages
import subprocess

setup(name="singer-python",
      version='6.0.1',
      description="Singer.io utility library",
      author="Stitch",
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      url="http://singer.io",
      install_requires=[
          'pytz>=2024.1',
          'jsonschema>=2.6.0,==2.*',
          'simplejson>=3.19.2,==3.*',
          'python-dateutil>=2.8.2,==2.*',
          'backoff>=2.2.1,==2.*',
          'ciso8601>=2.3.1,==2.*',
      ],
      extras_require={
          'dev': [
              'pylint',
              'ipython',
              'ipdb',
              'singer-tools'
          ]
      },
      packages=find_packages(),
      package_data = {
          'singer': [
              'logging.conf'
              ]
          },
)
