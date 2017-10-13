#!/usr/bin/env python

import sys
from setuptools import setup

install_requires = [
    "catsql >= 0.4.1"
]

if sys.version_info[0] == 2:
    install_requires.append('unicodecsv')

setup(name="emacsql",
      version="0.1.1",
      author="Paul Fitzpatrick",
      author_email="paulfitz@alum.mit.edu",
      description="Edit a slice of a SQL database in emacs",
      packages=['emacsql'],
      entry_points={
          "console_scripts": [
              "emacsql=emacsql.main:main"
          ]
      },
      install_requires=install_requires,
      url="https://github.com/paulfitz/emacsql"
)
