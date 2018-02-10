# -*- coding: utf-8 -*-
# Copyright 2018 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
"""
调试器
"""
import pdb
import os.path
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../euler'))
sys.path.append(path)

from problems import Problem  # noqa

if __name__ == "__main__":
    pdb.run('Problem(2).run()')
