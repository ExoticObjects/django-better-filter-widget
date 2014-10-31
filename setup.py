#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-better-filter-widget',
    version='0.2',
    author='Exotic Objects LLC',
    author_email='git@extc.co',
    license='MIT',
    url='https://github.com/ExoticObjects/django-better-filter-widget',
    include_package_data=True,
    long_description=open('README.md').read(),
    packages=find_packages(),
)