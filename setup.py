#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-better-filter-widget',
    version='0.4.1',
    author='Exotic Objects LLC',
    author_email='git@extc.co',
    license='MIT',
    url='https://github.com/ExoticObjects/django-better-filter-widget',
    include_package_data=True,
    long_description=open('README.md').read(),
    description='A better filter widget for foreign key relationships',
    packages=find_packages(),
)
