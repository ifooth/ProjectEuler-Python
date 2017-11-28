# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
import inspect
import os.path
import re

from euler import settings

module_pattern = re.compile(r'^(?P<name>problem_\d+_\d+).py$')
func_pattern = re.compile(r'^problem_(?P<p_id>\d+)$')


class ResultNotFound(Exception):
    pass


def load_problems():
    """动态加载题目
    """
    problem_func = {}
    for file_name in os.listdir(os.path.join(settings.BASE_DIR, 'euler/problems')):
        module = module_pattern.match(file_name)
        if module:
            m = __import__('euler.problems.%s' % module.groupdict()['name'])
            all_members = inspect.getmembers(
                getattr(m.problems, module.groupdict()['name']))
            func = dict(filter(
                lambda x: func_pattern.match(x[0]), all_members))
            problem_func.update(func)
    return problem_func


PROBLEM_FUNC = load_problems()


def get_file(filename):
    """Return filename from data directory."""
    datadir = os.path.join(settings.BASE_DIR, 'euler/data')

    with open(os.path.join(datadir, filename), 'r') as fh:
        return fh.read()


def get_result(problem_id):
    """返回结果
    """
    data = [i.strip() for i in get_file('euler_results.dat').splitlines()]
    try:
        result = data[problem_id - 1]
        if result:
            return int(result)
        else:
            raise ResultNotFound('have empty result')
    except IndexError:
        raise ResultNotFound('have no result')
