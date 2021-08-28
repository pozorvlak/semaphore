#!/usr/bin/env python

from distutils.core import setup

setup(
    name='sync',
    version='0.0.1',
    description='Simulator for The Little Book of Semaphores',
    author='Allen Downey',
    py_modules=['sync'],
    scripts=['scripts/sync']
)
