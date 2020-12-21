
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# package setup
#
# ------------------------------------------------

# imports
# -------
import os

# config
# ------
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

# requirements
# ------------
with open('requirements.txt') as f:
    REQUIREMENTS = f.read().strip().split('\n')

if os.path.exists('README.md'):
    long_description = open('README.md').read()
else:
    long_description = 'GroMass - A scheduling service to transport and manipulate a large collection of GROMACS files'

TEST_REQUIREMENTS = [
    'pytest',
    'pytest-runner'
]

# exec
# ----
setup(
    name="gromass",
    version="0.0.1",
    packages=['gromass'],
    license='MIT',
    author="Suliman Sharif",
    author_email="sharifsuliman1@gmail.com",
    url="https://github.com/Shen-Group/LogReader",
    install_requires=REQUIREMENTS,
    long_description=long_description,
    long_description_content_type='text/markdown',
    zip_safe=False,
    keywords='logreader logs GROMACS',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=TEST_REQUIREMENTS,
)