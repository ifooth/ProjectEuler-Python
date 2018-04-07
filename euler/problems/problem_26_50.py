# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
import fractions
import functools
import itertools
import logging
import math
import operator

from euler.lib import _int, data

LOG = logging.getLogger(__name__)


def problem_26():
    """
    Reciprocal cycles
    倒数的循环节
    https://en.wikipedia.org/wiki/Repeating_decimal
    """
    cycles_count = 0
    cycles_num = 0
    for num in range(2, 1000):
        if num % 2 == 0 or num % 5 == 0:
            continue
        for count in itertools.count(1):
            if (10 ** count - 1) % num == 0:
                if count > cycles_count:
                    cycles_num = num
                    cycles_count = count
                break
    return cycles_num


def problem_27():
    """
    Quadratic primes
    二次“素数生成”多项式
    """
    max_a, max_b, max_count = 0, 0, 0
    for a in range(-1000, 1000):
        for b in range(-1000, 1000):
            for count in itertools.count(0):
                if not _int.is_prime(count ** 2 + a * count + b):
                    break
            if count > max_count:
                max_a, max_b, max_count = a, b, count
    return max_a * max_b


def problem_28():
    """
    Number spiral diagonals
    螺旋数阵对角线
    """
    start = 1
    sum_diagonals = 1
    for n in range(1, (1001 - 1) / 2 + 1):
        for count in range(4):
            start += 2 * n
            sum_diagonals += start
    return sum_diagonals


def problem_29():
    """
    Distinct powers
    不同的幂
    """
    return len(set(i ** j for i in range(2, 101) for j in range(2, 101)))


def problem_30():
    """
    Digit fifth powers
    各位数字的五次幂
    limit 9**5 * 4
    """
    return sum(filter(
        lambda num: num == sum(map(lambda x: int(x) ** 5, str(num))),
        range(2, 9 ** 5 * 7)))


def problem_31():
    """
    Coin sums
    硬币求和
    动态规划，背包问题(Knapsack problem)
    """
    target = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [1] + [0] * target
    for coin in coins:
        for i in range(coin, target + 1):
            ways[i] += ways[i - coin]
    return ways[target]


def problem_32():
    """
    Pandigital products
    全数字的乘积
    1, 判断全数字
    2，遍历所以9位数字(Limiting the Search Space)
    """
    pandigital = set()
    # 1位数 * 4位数
    for i in range(1, 9 + 1):
        for j in range(1234, 9876 + 1):
            num = i * j
            if _int.is_pandigital(str(i) + str(j) + str(num)):
                pandigital.add(num)
    # 2位数 * 3位数
    for i in range(12, 98 + 1):
        for j in range(123, 987 + 1):
            num = i * j
            if _int.is_pandigital(str(i) + str(j) + str(num)):
                pandigital.add(num)
    return sum(pandigital)


def problem_33():
    """
    Digit cancelling fractions
    消去数字的分数
    平凡解(trivial)/非平凡解(non-trivial)
    49/98是一个非平凡解, 30/50是一个平凡解
    x * y / y * z(x < z)
    """
    result = 1
    for i in range(1, 10):
        for j in range(i + 1, 10):
            for k in range(1, 10):
                if fractions.Fraction(i * 10 + j, j * 10 + k) == fractions.Fraction(i, k):  # noqa
                    result *= fractions.Fraction(i, k)
    return result.denominator


def problem_34():
    """
    Digit factorials
    各位数字的阶乘
    分析范围:
    [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    上限 9! * 7(还是没懂)
    """
    factorials = [math.factorial(i) for i in range(0, 10)]
    return sum(i for i in range(3, math.factorial(9) * 7) if sum(factorials[int(j)] for j in str(i)) == i)  # noqa


def problem_35():
    """
    Circular primes
    圆周素数
    """
    total_count = 13
    for num in range(100, 1000000):
        num = str(num)
        if any(i in num for i in '02468'):
            continue
        num_length = len(num)
        while num_length:
            num = num[1:] + num[0]
            if not _int.is_prime(int(num)):
                break
            num_length -= 1
        else:
            total_count += 1
    return total_count


def problem_36():
    """
    Double-base palindromes
    双进制回文数
    """
    return sum(filter(
        lambda x: _int.is_palindromic(x) and _int.is_palindromic(bin(x)[2:]),
        range(1, 1000000)))


def problem_37():
    """
    Truncatable primes
    可截素数
    http://en.wikipedia.org/wiki/Truncatable_prime
    """
    count = 0
    truncatable_prime = []
    for prime in _int.prime_sieve():
        if prime in [2, 3, 5, 7]:
            continue
        left_prime = list(str(prime)[1:])
        while left_prime:
            if not _int.is_prime(int(''.join(left_prime))):
                break
            left_prime.pop(0)
        else:
            right_prime = list(str(prime)[:-1])
            while right_prime:
                if not _int.is_prime(int(''.join(right_prime))):
                    break
                right_prime.pop(-1)
            else:
                LOG.debug('truncatable_prime %s', prime)
                count += 1
                truncatable_prime.append(prime)
                if count == 11:
                    return sum(truncatable_prime)


def problem_38():
    """
    Pandigital multiples
    全数字的倍数
    分析：n=2
    """
    for i in range(9876, 9234, -1):
        num = str(i) + str(i * 2)
        if _int.is_pandigital(int(num)):
            return int(num)


def problem_39():
    """
    nteger right triangles
    整数边长直角三角形
    """
    solutions = iter(
        (x, y, z)
        for x in range(4, 500)
        for y in range(x, 500)
        for z in range(y, 500)
        if x ** 2 + y ** 2 == z ** 2 and x + y + z <= 1000)
    max_p = {}
    for i in solutions:
        p = sum(i)
        max_p[p] = max_p.get(p, 0) + 1
    return max(max_p.items(), key=lambda x: x[1])[0]

    # max_solutions = 0
    # max_p = 0
    # for p in range(2, 1001):
    #     solutions = 0
    #     for x in range(min(p, 500)):
    #         for y in range(x, min(p, 500)):
    #             z = p - x - y
    #             if z <= 0:
    #                 break
    #             if x ** 2 + y ** 2 == z ** 2:
    #                 solutions += 1
    #     if solutions > max_solutions:
    #         max_solutions = solutions
    #         max_p = p

    return max_p


def problem_40():
    """
    Champernowne’s constant
    钱珀瑙恩常数
    """
    champernowne = ''
    for i in itertools.count(1):
        champernowne += str(i)
        if len(champernowne) >= 1000000:
            return functools.reduce(
                operator.mul,
                map(int, [champernowne[10 ** i - 1] for i in range(1, 7)]))


def problem_41():
    """
    Pandigital prime
    全数字的素数
    """
    letters = '123456789'
    for i in range(9, 0, -1):
        _letters = letters[:i][::-1]
        for j in itertools.permutations(_letters, i):
            num = int(''.join(j))
            if _int.is_prime(num):
                return num


def problem_42():
    """
    Coded triangle numbers
    编码三角形数
    """
    words = [i.strip('"') for i in data.get_file('words.txt').split(',')]
    words_ord_sum = map(
        lambda word: sum(map(lambda x: ord(x) - 64, word)),
        words)
    return len(filter(lambda x: _int.is_triangle(x), words_ord_sum))


def problem_43():
    """
    Sub-string divisibility
    子串的可整除性
    """
    letters = '0123456789'
    sum_sub = 0
    primes = [2, 3, 5, 7, 11, 13, 17]
    for letter in itertools.permutations(letters, 10):
        if letter[0] == '0':
            continue
        num = ''.join(letter)
        m = 0
        while m != 7:
            if int(num[m + 1: m + 4]) % primes[m] != 0:
                break
            m += 1
        else:
            sum_sub += int(num)
    return sum_sub


def problem_44():
    """
    Pentagon numbers
    五边形数
    第一个即最小的
    """
    pentagon_numbers = []
    for n in itertools.count(1):
        pentagon = _int.pentagon(n)
        for i in pentagon_numbers:
            difference = pentagon - i
            if _int.is_pentagon(i + pentagon) and _int.is_pentagon(difference):
                LOG.debug('pentagon %s, %s', i, pentagon)
                return difference
        pentagon_numbers.append(pentagon)


def problem_45():
    """
    Triangular, pentagonal, and hexagonal
    三角形数、五边形数和六角形数
    """
    num = 286
    while True:
        _triangle = _int.triangle(num)
        if _int.is_pentagon(_triangle) and _int.is_hexagon(_triangle):
            return _triangle
        num += 1


def problem_46():
    """
    Goldbach’s other conjecture
    哥德巴赫的另一个猜想
    """
    n = 33
    primes = []
    while True:
        if all(n % p for p in primes):
            primes.append(n)
        else:
            if not any((n - 2 * i * i) in primes for i in range(1, n)):
                break
        n += 2
    return n


def problem_47():
    """
    Distinct primes factors
    不同的质因数
    """
    consecutive_number = 1
    count = 0
    consecutive = 4
    while count < consecutive:
        consecutive_number += 1
        if len(_int.factors(consecutive_number).keys()) - 1 == consecutive:
            count += 1
        else:
            count = 0
    return consecutive_number - consecutive + 1


def problem_48():
    """
    Self powers
    自幂
    """
    return int(str(sum(i ** i for i in range(1, 1001)))[-10:])


def problem_49():
    """
    Prime permutations
    素数重排
    """
    prime_permutations = {}
    primes = list(
        itertools.takewhile(lambda x: x < 10000, _int.prime_sieve()))
    for i in primes:
        key = ''.join(sorted(str(i)))
        if key == '1478':
            continue
        if key != 4:
            continue
        if key in prime_permutations:
            prime_permutations[key].append(i)
        else:
            prime_permutations[key] = [i]

    for key, primes in prime_permutations.items():
        if len(primes) < 3:
            continue
        for i in range(len(primes) - 2):
            permutations = primes[i: i + 3]
            if permutations[2] - permutations[1] == permutations[1] - permutations[0]:  # noqa
                LOG.debug('prime_permutations %s', permutations)
                return ''.join(map(str, permutations))


def problem_50():
    """
    Consecutive prime sum
    连续素数的和
    """
    consecutive_prime = []
    all_prime = list(
        itertools.takewhile(lambda x: x < 1000000, _int.prime_sieve()))
    # 分析上限
    max_count = 0
    prime_sum = 0
    while prime_sum < 1000000:
        prime_sum += all_prime[max_count]
        max_count += 1

    for i in range(max_count, 0, -1):
        for j in range(max_count - i):
            consecutive_prime = all_prime[j: i + j]
            if sum(consecutive_prime) in all_prime:
                LOG.debug('consecutive_prime %s', consecutive_prime)
                return sum(consecutive_prime)
