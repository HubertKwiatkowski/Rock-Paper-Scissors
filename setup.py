#!/usr/bin/env python3

from os.path import join, dirname
from setuptools import setup

requirements = open(join(dirname(__file__), 'requirements.txt')).readlines()

setup(
    name='rps',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'rock-paper-scissors=rps.__main__:run'
        ]
    }
)
