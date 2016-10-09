# -*- coding: utf-8 -*-
# Copyright 2016 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
import functools
import itertools
import logging
import math
import operator


LOG = logging.getLogger(__name__)


def is_prime(num):
    """素数检测法
    """
    if num < 2:
        return False
    if num % 2 == 0 and num != 2:
        return False
    if num % 3 == 0 and num != 3:
        return False
    if any((num % i) == 0 or (num % (i + 2)) == 0 for i in range(5, int(math.sqrt(num)) + 2, 6)):  # noqa
        return False
    return True


def is_palindromic(num):
    """回文数 9009
    """
    _num = str(num)
    return _num == _num[::-1]


def is_pandigital(num, n=9):
    """
    Pandigital number
    全数字
    """
    n_letters = '123456789'
    str_num = str(num)
    set_num = set(str_num)
    if len(str_num) != len(set_num):
        return False
    return n_letters[:n] == ''.join(sorted(set_num))


def factors_generator(num):
    """因子生成器
    12 = 1 * 2 * 2 * 3
    """
    yield 1
    factor, limit = 2, math.sqrt(num)
    while factor <= limit:
        if num % factor == 0:
            yield factor
            num //= factor
            limit = math.sqrt(num)
        else:
            factor += 1
    if num > 1:
        yield num


def factors(num):
    """
    因数分解 12 = 1^1 * 2^2 * 3^1
    return {1: 1, 2: 2, : 3: 1}
    """
    _factors = {}
    for i in factors_generator(num):
        _factors[i] = _factors.get(i, 0) + 1
    LOG.debug('%s factors is: %s', num, _factors)
    return _factors


def positive_divisors(num):
    """
    返回所有正因子
    12 = [1, 2, 3, 4, 6, 12]
    partially ordered 偏序关系
    Hasse diagram 哈斯图
    """
    _factors = list(factors_generator(num))
    total_divisor = [(1, 1), (1, num)]
    for i in range(2, len(_factors)):
        total_divisor.extend(itertools.combinations(_factors, i))
    total_divisor = list(set(map(
        lambda x: functools.reduce(operator.mul, x), total_divisor)))
    LOG.debug('%s divisor: %s', num, total_divisor)
    return total_divisor


def proper_divisors(num):
    """
    真因子 小于n且整除n的正整数
    不包含自己
    12 = [1, 2, 3, 4, 6]
    """
    _factors = factors(num)
    divisors = [1]
    for prime, power in _factors.items():
        divisors = [d * prime ** p for d in divisors for p in range(power + 1)]
    divisors = list(set(divisors))
    divisors.remove(num)
    return divisors


def fibonacci_generator(fib_1=1, fib_2=1):
    """斐波那契数生成器
    F1 = fib_1
    F2 = fib_2
    Fn = Fn−1 + Fn−2
    """
    yield fib_1
    yield fib_2

    while True:
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        yield fib_2


def phi(num):
    """在小于n的数中，与n互质的数的数目为欧拉函数
    """
    _factors = factors(num)
    result = 1
    # 欧拉函数计算从2开始
    _factors.pop(1)
    for prime, power in _factors.items():
        result *= prime ** (power - 1) * (prime - 1)
    return result
    # 使用函数式写法
    # return functools.reduce(
    #     operator.mul,
    #     map(lambda x: x[0] ** (x[1] - 1) * (x[0] - 1), _factors.items()))


def prime_sieve():
    """
    查找一个区间内的素数
    算法：Sieve of Eratosthenes
    根据性质：一个素数的各个倍数，是一个差为此素数本身的等差数列
    """
    composites = {}
    for num in itertools.count(2):
        prime = composites.pop(num, None)
        if prime is None:
            yield num  # num是一个素数
            composites[num * num] = num
            LOG.debug('%s, composites: %s', num, composites)
        else:
            composite = num + prime  # num是一个合数
            while composite in composites:
                composite += prime
            composites[composite] = prime
            LOG.debug('%s, composites: %s', num, composites)


def triangle(num):
    """
    三角形数
    """
    return num * (num + 1) / 2


def square(num):
    """
    正方形数
    """
    return num * num


def pentagon(num):
    """
    五边形数
    """
    return num * (3 * num - 1) / 2


def hexagon(num):
    """
    六边形数
    """
    return num * (2 * num - 1)


def heptagon(num):
    """
    七边型数
    """
    return num * (5 * num - 3) / 2


def octagon(num):
    """
    八边型数
    """
    return num * (3 * num - 2)


def is_triangle(num):
    """
    判断三角形数
    """
    solution = (-1 + math.sqrt((1 + 8 * num))) / 2.0
    return int(solution) == solution


def is_square(num):
    """
    判断正方形数
    """
    solution = math.sqrt(num)
    return int(solution) == solution


def is_pentagon(num):
    """
    判断五边形数
    """
    solution = (1 + math.sqrt(1 + 24 * num)) / 6.0
    return int(solution) == solution


def is_hexagon(num):
    """
    判断六边形数
    """
    solution = (1 + math.sqrt(1 + 8 * num)) / 4.0
    return int(solution) == solution


def is_heptagon(num):
    """
    判断七边型数
    """
    solution = (3 + math.sqrt(9 + 40 * num)) / 10.0
    return int(solution) == solution


def is_octagon(num):
    """
    判断八边型数
    """
    solution = (2 + math.sqrt(4 + 12 * num)) / 6.0
    return int(solution) == solution
