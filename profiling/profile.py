# -*- coding: utf-8 -*-
# Copyright 2018 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
"""
性能测试
"""
import logging
import cProfile
import os.path
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../euler'))
sys.path.append(path)


log = logging.getLogger(__file__)


def euler_profile(num=1):
    p = 'Problem(%s).run()' % num
    cProfile.run(p)


if __name__ == "__main__":
    euler_profile()
