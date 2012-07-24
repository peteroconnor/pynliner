#!/usr/bin/env python

from distutils.core import setup

setup(name='pynliner',
      version='0.4.1',
      description='Python CSS-to-inline-styles conversion tool for HTML using BeautifulSoup and cssutils',
      author='Tanner Netterville, Peter OConnor',
      author_email='tannern@gmail.com, peter.k.oconnor@gmail.com',
      packages=('pynliner',),
      requires=('BeautifulSoup(<4.0)',
                'cssutils(>=0.9.7)',
                ),
      provides=('pynliner',),
     )
