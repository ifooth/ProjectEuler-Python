# -*- coding: utf-8 -*-
# Copyright 2018 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
import logging

from euler.lib import _int, data, util
from pprint import pprint

logger = logging.getLogger(__name__)


def problem_111():

    def str2dict(num):
        data = {}
        for n in str(num):
            data[n] = data.get(n, 0) + 1
        return data

    data = {str(i): {'M': 0, 'N': 0, 'S': 0} for i in range(0, 10)}
    logger.debug(data)

    k = 6
    k_min, k_max = 10 ** (k - 1), 10 ** k

    for i in _int.prime_sieve():
        if i < k_min:
            continue
        if i > k_max:
            break

        num = str2dict(i)

        for k, v in num.items():
            if data[k]['M'] < v:
                data[k]['M'] = v
                data[k]['N'] = 1
                data[k]['S'] = i
            elif data[k]['M'] == v:
                data[k]['N'] += 1
                data[k]['S'] += i
        logger.debug(data)

    pprint(data)
    s = sum(i['S'] for i in data.values())
    return s


def problem_108():
    return data.openfile("names.txt").__next__()


def problem_103():
    pass


def problem_113():
    n = 100
    return util.binomial(n + 10, 10) + util.binomial(n + 9, 9) - 10 * n - 2


def problem_116():
    color = [2, 3, 4]
    limit = 50
    num = 0
    i = 0
    while i < 3:
        k = 1
        while k * color[i] < limit:
            num += ((limit - color[i] * k) * k + 1)
            k += 1
        i += 1
    return num


def problem_117():
    color = [2, 3, 4]
    limit = 5
    num = 1
    i = 0
    while i < 3:
        k = 1
        while k * color[i] < limit:
            num += ((limit - (color[i] * k)) * k + 1)
            k += 1
        i += 1
    a = {2: limit // 2, 3: limit // 3, 4: limit // 4}
    return a
    return num
