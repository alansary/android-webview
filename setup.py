# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='android-webview',
    version='0.1',
    description='Python script to generate android webview based apps',
    author='Rael Max',
    author_email='contato@raelmax.com',
    url='https://github.com/raelmax/android-webview',
    packages=['android-webview'],
    package_data={
        'android-webview': ['templates/*'],
    },
    test_suite='tests.suite'
)

