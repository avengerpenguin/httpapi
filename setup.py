#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
    name='httpapi',
    use_scm_version={
        'local_scheme': 'dirty-tag',
        'write_to': 'httpapi/_version.py',
        'fallback_version': '0.0.0',
    },
    description='Pythonic helpers for HTTP APIs with long URLs.',
    author='Ross Fenning',
    author_email='github@rossfenning.co.uk',
    url='https://github.com/avengerpenguin/httpapi',
    packages=find_packages('httpapi'),
    package_dir={'': 'httpapi'},
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP',
    ],
    project_urls={
        'Issue Tracker': 'https://github.com/avengerpenguin/httpapi/issues',
    },
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    setup_requires=[
        'pytest-runner',
        'setuptools_scm>=3.3.1',
    ],
)
