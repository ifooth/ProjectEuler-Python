# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
import argparse
import inspect
import logging
import os
import re
import sys
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from euler import settings  # noqa
from euler.lib import data

PROBLEM_FUNC = {}
module_pattern = re.compile(r'^(?P<name>problem_\d+_\d+).py$')
func_pattern = re.compile(r'^problem_(?P<p_id>\d+)$')

LOG = logging.getLogger('euler.__main__')


def load_problems():
    """动态加载题目
    """
    for file_name in os.listdir(os.path.join(BASE_DIR, 'euler/problems')):
        module = module_pattern.match(file_name)
        if module:
            m = __import__('euler.problems.%s' % module.groupdict()['name'])
            all_members = inspect.getmembers(
                getattr(m.problems, module.groupdict()['name']))
            func = dict(filter(
                lambda x: func_pattern.match(x[0]), all_members))
            PROBLEM_FUNC.update(func)

load_problems()


def main():
    parser = argparse.ArgumentParser(
        description='EulerProject problem launcher')
    parser.add_argument('problem', metavar='id', type=int, nargs=1,
                        help='run problem')
    args = parser.parse_args()

    name = 'problem_%s' % args.problem[0]
    if name not in PROBLEM_FUNC:
        LOG.error('not found %s' % name)
        sys.exit(1)
    start = time.time()
    try:
        result = PROBLEM_FUNC[name]()
    except KeyboardInterrupt:
        result = 'Interrupted'
    LOG.info(
        '%s, use %.3f(s), euler: %s', result, time.time() - start,
        data.get_result(args.problem[0]))


if __name__ == "__main__":
    main()
