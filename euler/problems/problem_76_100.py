# -*- coding: utf-8 -*-
# Copyright 2016 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
import decimal
import logging
from collections import OrderedDict

from euler.lib import _int
from euler.lib import data

LOG = logging.getLogger(__name__)


def problem_76():
    """
    Counting summations
    加和计数
    算法：动态规划，背包问题(Knapsack problem),类似31题
    """
    target = 100
    coins = range(1, 100)
    ways = [1] + [0] * target
    for coin in coins:
        for i in range(coin, target + 1):
            ways[i] += ways[i - coin]
    return ways[target]


def problem_77():
    """
    Prime summations
    素数加和
    算法：动态规划，背包问题(Knapsack problem),类似31, 76题
    """
    primes = []
    target = 10
    for prime in _int.prime_sieve():
        if prime > target:
            return
        primes.append(prime)
        ways = [0] + [0] * target
        print primes
        for coin in primes:
            for i in range(coin, target + 1):
                ways[i] += ways[i - coin]
        print ways[target]


def problem_79():
    mydata=[i.strip() for i in data.openfile('keylog.txt')]
    key=mydata[0]

def problem_80():
    decimal.getcontext().prec=102
    i_sum=0
    l_temp=set(i*i for i in range(1,10))
    for i in filter(lambda x:x not in l_temp,range(2,100)):
        if i in l_temp:continue
        i_sum+=sum(int(i) for i in str((decimal.Decimal(i).sqrt()*10**99))[0:100:1])
        #print(str((decimal.Decimal(i).sqrt()*10**99)))
    return i_sum


def problem_81():
    """
    Path sum: two ways
    路径和：两个方向
    算法
    先消掉最下面一行，最消掉最后一列
    计算最后个数字
    参考：18题
    进一步思考，可以转换成树结构，
    往下为数的左节点，右为右节点，构造如下
    1
    4 2
    7 5 3
    8 6
    9
    """
    matrix = data.get_file('p081_matrix.txt').strip().splitlines()
    matrix = [[int(j) for j in i.split(',')] for i in matrix]

    def help_func(_data):
        depth = len(_data)
        if depth == 1:
            return _data
        # 计算下面倒数第二行最小值
        row = depth - 2
        for column in range(row, -1, -1):
            _data[row][column] += min(_data[row + 1][column],
                                      _data[row][column + 1])
        # 计算右侧倒数第二列最小值
        column = depth - 2
        # 最下面一行上面已经计算，不能重复计算
        for row in range(column - 1, -1, -1):
            _data[row][column] += min(_data[row][column + 1],
                                      _data[row + 1][column])
        # 计算完毕，清空最外面一层，可以优化
        _data = [[j for j in i[:depth - 1]] for i in _data[:depth - 1]]

        return help_func(_data)

    # 计算最外一层，初始值，消掉第一个数
    depth = len(matrix) - 1
    for i in range(depth, 0, -1):
        matrix[depth][i - 1] += matrix[depth][i]
        matrix[i - 1][depth] += matrix[i][depth]

    _data = help_func(matrix)
    return _data[0][0]


def problem_89():
    roman_num = data.openfile('roman.txt').split('\n')
    roman_len = sum(len(i) for i in roman_num)
    roman_new = [num2roman(roman2num(i)) for i in roman_num]
    roman_len_new = sum(len(i) for i in roman_new)
    n = 'XIIIIII'
    log.info(n)
    log.info(roman2num(n))
    log.info(num2roman(roman2num(n)))
    return roman_len_new - roman_len

def roman2num(roman):
    roman_chars = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    return sum(roman_chars[i] for i in str(roman))

def num2roman(num):
    roman_chars = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    roman_chars = OrderedDict(sorted(roman_chars.items(),key=lambda x:x[1],reverse=True))
    result = ''
    for r in roman_chars:
        a,b = divmod(num,roman_chars[r])
        num = b
        result += r*a
    return result


def problem_92():
    """
    Square digit chains
    平方数字链
    """
    chains = set()
    for num in range(2, 10000000):
        digit = num
        while num != 89:
            if num == 1:
                break
            num = sum(int(i) ** 2 for i in str(num))
            if num in chains:
                chains.add(digit)
                break
        else:
            chains.add(num)
    return len(chains)


def problem_95():
    """
    Amicable chains
    亲和数链
    参考21题
    """
    min_chains = [0, 0]
    for num in range(12496, 12499):
        chains = [num]
        while True:
            num = sum(_int.proper_divisors(num))
            print num
            if num == 1:
                print chains[0]
                break
            if num not in chains:
                chains.append(num)
            elif num == chains[0] and len(chains) > min_chains[0]:
                min_chains[0] = len(chains)
                min_chains[1] = min(chains)
                print chains[0], chains
                break
            else:
                print chains[0]
                break
    return chains
