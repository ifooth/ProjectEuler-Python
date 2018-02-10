# -*- coding: utf-8 -*-
# Copyright 2016 Tencent
# Author: Joe Lei <joelei@tencent.com>
from distutils.core import setup


packages, data_files = [], []


with open('README.md') as fp:
    long_description = fp.read()


setup(
    name='ProjectEuler-Python',
    version='0.0.3',
    description='project euler problem solve by python',
    long_description=long_description,
    author='Joe Lei',
    author_email='thezero12@hotmail.com',
    url='https://github.com/ifooth/ProjectEuler-Python',
    packages=['euler'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
)
