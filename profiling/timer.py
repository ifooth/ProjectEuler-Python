# -*- coding: utf-8 -*-
# Copyright 2016 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
from timeit import Timer
import logging
import os.path
import sys
import itertools


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)


from euler.lib import _int


LOG = logging.getLogger(__file__)


def run_timer(num):
    i = [_int.is_prime(j) for j in range(1000000)]


if __name__=="__main__":
    t = Timer('run_timer(2)', setup='from __main__ import run_timer')
    print(t.timeit(number=1))
