#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from codecs import open
from os import path

with open(path.join('./', 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

INSTALL_REQUIRES = (['requests','jsonpickle'])

setup(
    name='nevada',
    version='1.0.1',
    description='For those who want to use Naver Search Ad easily.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Taegyu Min, Junho Song',
    author_email='minimax@snu.ac.kr',
    url='https://github.com/taegyumin/python_nevada',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries',
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only'
    ],
    packages=find_packages(),
    keywords=['python_nevada', 'naver', 'search', 'ad'],
    python_requires='>=3.4',
    package_data={},
    install_requires=INSTALL_REQUIRES
)
