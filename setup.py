# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import os
from distutils.core import setup

version = open(os.path.join("sc", "mailchimp", "api", "version.txt")).read().strip()

setup(name='sc.mailchimp.api',
      version=version,
      description="Python wrapper for the MailChimp API",
      long_description=open(os.path.join("sc", "mailchimp", "api", "README.txt")).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Python mailchimp api',
      author='Simples Consultoria',
      author_email='products@simplesconsultoria.com.br',
      url='http://www.simplesconsultoria.com.br/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['sc', 'sc.mailchimp'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'simplejson',
      ],
      paster_plugins = ["ZopeSkel"],
      )
