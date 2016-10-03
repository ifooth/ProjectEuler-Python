# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
import operator
import math


def accumulate(iterable, func=operator.add):
    """
    Return running totals
    accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
    """

    it = iter(iterable)
    try:
        total = next(it)
    except StopIteration:
        return
    yield total
    for element in it:
        total = func(total, element)
        yield total


def combinations(n, k):
    """
    组合数
    C(n, k) = n! / (k! * (n - k)!) k <= n
    """
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
