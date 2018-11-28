# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
import os.path

datadir = os.path.join(os.path.dirname(__file__), '../data')


def get_file(filename):
    """Return filename from data directory."""
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
            return 'had empty result'
    except IndexError:
        return 'have no result'
