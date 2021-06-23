#!/usr/bin/env python
from setuptools import setup

NAME = "httpapi"
setup(
    name=NAME,
    use_scm_version={
        "local_scheme": "dirty-tag",
        "write_to": f"{NAME}/_version.py",
        "fallback_version": "0.0.0",
    },
    author="Ross Fenning",
    author_email="github@rossfenning.co.uk",
    packages=[NAME],
    description="Pythonic helpers for HTTP APIs with long URLs.",
    setup_requires=[
        "setuptools_scm>=3.3.1",
        "pre-commit",
    ],
    install_requires=["requests"],
    extras_require={
        "test": [
            "pytest",
            "httpretty",
            "testypie>=1.2.2",
            "pytest-pikachu",
            "pytest-mypy",
            "types-requests",
        ],
    },
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet :: WWW/HTTP",
    ],
    project_urls={
        "Issue Tracker": "https://github.com/avengerpenguin/httpapi/issues",
    },
)
