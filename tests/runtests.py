# -*- coding: utf-8 -*-
# Copyright 2017 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
import logging
import os.path
import sys
import time
import unittest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from euler.utils import loader

LOG = logging.getLogger(__name__)


class TestEuler(unittest.TestCase):
    pass


def test_generator(func, result):
    def test(self):
        start = time.time()
        func_result = func()
        print('run %s use %.3f(s)' % (func.__name__, time.time() - start))

        self.assertEqual(func_result, result)
    return test


def init_test(test_case):
    for problem_name in sorted(loader.PROBLEM_FUNC, key=lambda x: int(x[8:])):
        p_id = int(problem_name[8:])
        p_func = loader.PROBLEM_FUNC[problem_name]
        try:
            result = loader.get_result(p_id)
        except:
            continue

        test = test_generator(p_func, result)

        setattr(test_case, 'test_%s' % problem_name, test)


if __name__ == "__main__":
    init_test(TestEuler)
    unittest.main()
