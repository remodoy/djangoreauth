#!/usr/bin/env python

from distutils.core import setup

setup(name='djangoreauth',
      version='0.2',
      description='Django application for ReAuth authentication',
      keywords='reauth django authentication',
      author='Remod Oy',
      include_package_data = True,
      author_email='reauth@remod.fi',
      url='https://github.com/remodoy/djangoreauth',
      packages=['djangoreauth', 'djangoreauth.templatetags', 'djangoreauth.migrations'],
      license="MIT",
      package_dir={
        'djangoreauth': 'djangoreauth',
        'djangoreauth.templatetags': 'djangoreauth/templatetags',
        'djangoreauth.migrations': 'djangoreauth/migrations',
      },
      package_data={
        'djangoreauth': ['djangoreauth/static/js/polyfill.bundle.js', 'djangoreauth/static/js/reauth.bundle.js'],
      },
      requires=["django (>=1.8)"],
      classifiers=[
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
      ],
      )
