# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
import argparse
import logging
import sys
import time

from euler.utils import loader

logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description='EulerProject problem launcher')
    parser.add_argument('problem', metavar='id', type=int, nargs=1,
                        help='run problem')
    args = parser.parse_args()

    name = 'problem_%s' % args.problem[0]
    if name not in loader.PROBLEM_FUNC:
        logger.error('not found %s' % name)
        sys.exit(1)

    try:
        answer = loader.get_result(args.problem[0])
    except loader.ResultNotFound as error:
        logger.warning("problem %d %s.", args.problem[0], error)
        answer = '--'

    start = time.time()
    try:
        result = loader.PROBLEM_FUNC[name]()
    except KeyboardInterrupt:
        result = 'Interrupted'

    logger.info('%s, use %.3f(s), euler: %s', result, time.time() - start, answer)


if __name__ == "__main__":
    main()
