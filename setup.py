#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
import os
import re

root_dir = os.path.abspath(os.path.dirname(__file__))


def get_version(package_name):
    version_re = re.compile(r"^__version__ = [\"']([\w_.-]+)[\"']$")
    package_components = package_name.split('.')
    path_components = package_components + ['__init__.py']
    with open(os.path.join(root_dir, *path_components)) as f:
        for line in f:
            match = version_re.match(line[:-1])
            if match:
                return match.groups()[0]
    return '0.1.0'


PACKAGE = 'kaoz'


setup(
    name="kaoz",
    version=get_version(PACKAGE),
    author="Binet Réseau",
    author_email="br@eleves.polytechnique.fr",
    description="A simple IRC notifier bot.",
    license="MIT",
    keywords=['irc', 'notification', 'bot'],
    url="http://github.com/BinetReseau/Kaoz",
    download_url="http://pypi.python.org/pypi/kaoz/",
    packages=find_packages(),
    install_requires=[
        'distribute',
        'twisted',
    ],
    scripts=[
        'bin/kaoz',
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: No Input/Output (Daemon)",
        "Framework :: Twisted",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Topic :: Communications :: Chat :: Internet Relay Chat",
        "Topic :: System :: Logging",
        "Topic :: System :: Monitoring",
        'Operating System :: Unix',
        'Programming Language :: Python',
    ],
#    test_suite='tests',
)
