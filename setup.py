#!/usr/bin/env python

from distutils.core import setup

setup(name='djangoreauth',
      version='0.1',
      description='Django application for ReAuth authentication',
      keywords='reauth django authentication',
      author='Remod Oy',
      author_email='reauth@remod.fi',
      url='https://www.remod.fi/reauth',
      packages=['djangoreauth'],
      license="MIT",
      package_dir={'djangoreauth': 'djangoreauth'},
      requires=["django (>=1.8)"],
      classifiers=[
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
      ],
      )
