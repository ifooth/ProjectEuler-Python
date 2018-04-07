# -*- coding: utf-8 -*-
# Copyright 2018 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
import logging
import itertools

from euler.lib import _int, data, util
from pprint import pprint

logger = logging.getLogger(__name__)


def problem_111():
    data = {str(i): {'M': 0, 'N': 0, 'S': 0} for i in range(0, 10)}
    logger.debug(data)

    k = 7
    # k_min, k_max = 10 ** (k - 1), 10 ** k
    # cache = set()
    # for i in _int.prime_sieve():
    #     if i < k_min:
    #         continue
    #     if i > k_max:
    #         break
    #     cache.add(i)

    for i in itertools.product('1023456789', repeat=k):
        if '0' == i[0]:
            continue
        n = int(''.join(i))
        num = _int.letter_count(i)
        is_prime = None
        for k, v in num.items():
            if data[k]['M'] < v:
                if is_prime is None:
                    is_prime = _int.is_prime(n)
                if is_prime is False:
                    break

                data[k]['M'] = v
                data[k]['N'] = 1
                data[k]['S'] = n
            elif data[k]['M'] == v:
                if is_prime is None:
                    is_prime = _int.is_prime(n)
                if is_prime is False:
                    break

                data[k]['N'] += 1
                data[k]['S'] += n

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
