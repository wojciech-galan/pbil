#! /usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# requirements https://caremad.io/posts/2013/07/setup-vs-requirement/
# and https://packaging.python.org/requirements/
# versioning https://packaging.python.org/distributing/#semantic-versioning-preferred

setup(
    name="pbil",
    version='0.1.0',
    description='Population-based incremental learning in Python',
    url='https://github.com/wojciech-galan/pbil',
    author='Wojciech Gałan',
    license='GNU GPL v3.0',
    install_requires=[
        'numpy'
    ],
    packages=find_packages(),
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ]
)