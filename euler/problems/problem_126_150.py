# -*- coding: utf-8 -*-
# Copyright 2016 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
import itertools
import logging

from euler.lib import _int

LOG = logging.getLogger(__name__)


def problem_134():
    """
    Prime pair connection
    质数对连接
    """
    sum_prime = 0
    prime_first = 5
    count = 0
    for prime in _int.prime_sieve():
        if prime <= 5:
            continue
        if prime > 1000:
            break
        count += 1
        if count % 1000 == 0:
            print count, prime
        # for i in itertools.count(1):
        #     _prime = int(str(i) + str(prime_first))
        #     if _prime % prime == 0:
        #         LOG.debug('%s, %s, %s', prime, _prime, i)
        #         sum_prime += _prime
        #         prime_first = prime
        #         break
        _count = 0
        for i in itertools.count(3, 2):
            _count += 1
            if str(prime * i).endswith(str(prime_first)):
                LOG.info('%s, %s, %s', prime, prime * i, i)
                sum_prime += prime * i
                prime_first = prime
                break
    return sum_prime
