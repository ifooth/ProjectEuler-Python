# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
import argparse
import logging
import os
import sys
from euler import settings  # noqa


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from problems import Problem
from profiling import profile


LOG = logging.getLogger('euler.__main__')


def main():
    parser = argparse.ArgumentParser(description='euler commander')
    parser.add_argument('problem', metavar='num', type=int, nargs=1,
                        help='problem num')
    parser.add_argument('--test', metavar='num', type=int, nargs=1,
                        help='test num')
    parser.add_argument('--profile', metavar='num', type=int, nargs=1,
                        help='profile num')
    args = parser.parse_args()

    if args.problem:
        result = Problem(args.problem[0]).run()
        LOG.info(result)
    if args.profile:
        profile.euler_profile(args.profile[0])
    if args.test:
        pass

if __name__ == "__main__":
    main()
