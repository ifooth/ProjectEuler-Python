# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
import itertools
import logging
import math
import fractions

from euler.lib import data
from euler.lib import _int
from euler.lib import calc
from euler.lib import graph


LOG = logging.getLogger(__name__)


def problem_51():
    """
    Prime digit replacements
    素数数字替换
    """
    count = 6
    primes = []
    prime_length = 2

    def prime_family(primes):
        primes = map(lambda x: sorted(str(x)), primes)

    for prime in _int.prime_sieve():
        _len = len(str(prime))
        if _len == prime_length:
            primes.append(prime)
        if _len > prime_length:
            prime_family(primes)
            return primes


def problem_52():
    """
    Permuted multiples
    重排的倍数
    """
    for num in itertools.count(6):
        sorted_num = sorted(str(num))
        if any(sorted(str(num * i)) != sorted_num for i in range(2, 7)):
            continue
        return num


def problem_53():
    """
    Combinatoric selections
    组合数选择
    """
    count = 0
    for n in range(1, 101):
        for k in range(1, n + 1):
            if calc.combinations(n, k) > 1000000:
                count += 1
    return count


def problem_54():
    pokers = [i.split(' ') for i in data.get_file('poker.txt').split('\n')]
    return len(filter(lambda x: calc.Poker(x[:5]) > calc.Poker(x[5:]), pokers))


def problem_55():
    """
    Lychrel numbers
    利克瑞尔数
    """
    lychrel_numbers = 0
    for num in range(1, 10000):
        counter = 0
        while counter < 50:
            num = num + int((str(num)[::-1]))
            if _int.is_palindromic(num):
                break
            counter += 1
        else:
            lychrel_numbers += 1
    return lychrel_numbers


def problem_56():
    """
    Powerful Digit Sum
    幂的数字和
    """
    max_digit_sum = 0
    for i in range(1, 100):
        for j in range(1, 100):
            max_digit_sum = max(max_digit_sum, sum(map(int, str(i ** j))))
    return max_digit_sum


def problem_57(num=1000):
    """
    Square root convergents
    平方根逼近
    """
    init = fractions.Fraction(1, 2)
    n = 0
    for i in range(1000):
        init = 1 / (2 + init)
        if len(str((init + 1).numerator)) > len(str((init + 1).denominator)):
            n += 1
    return n


def problem_58(length=None):
    """
    Spiral primes
    螺旋素数
    """
    last_num = 1
    prime_count = 0
    total_num = 1
    for n in itertools.count(2):
        length_size = 2 * n - 1
        for i in range(1, 5):
            num = last_num + (length_size - 1) * i
            total_num += 1
            if _int.is_prime(num):
                prime_count += 1
            if prime_count * 1.0 / total_num < 0.1:
                return length_size
        last_num = num


def problem_59():
    """
    XOR decryption
    异或解密
    """
    keychars = 'abcdefghijklmnopqrstuvwxyz'
    keylen = 3
    ciphertext = list(data.get_file('cipher1.txt').strip().split(','))
    texts = ['', 0]
    a, b = divmod(len(ciphertext), 3)
    for i in itertools.product(keychars, repeat=keylen):
        cleartext = ''
        space = 0
        for j in range(a):
            for k in range(keylen):
                t = int(ciphertext[keylen * j + k]) ^ ord(i[k])
                if t == ord(' '):
                    space += 1
                cleartext += chr(t)
        if b:
            for k in range(b):
                t = int(ciphertext[keylen * a + k]) ^ ord(i[k])
                if t == ord(' '):
                    space += 1
                cleartext += chr(t)
        # 空格最多的就是解，我操
        if space > texts[1]:
            texts[1] = space
            texts[0] = cleartext
    return sum([ord(i) for i in texts[0]])


def problem_60():
    """
    Prime pair sets
    素数对的集合
    """
    prime_graph = {}
    for prime in _int.prime_sieve():
        prime_graph[prime] = []
        for i in prime_graph.keys():
            if (_int.is_prime(int(str(i) + str(prime))) and
                    _int.is_prime(int(str(prime) + str(i)))):

                # 组成无向图
                prime_graph[i].append(prime)
                prime_graph[prime].append(i)

        for j in itertools.combinations(prime_graph[prime], 4):
            if graph.is_connect(prime_graph, j):
                return sum(list(j) + [prime])


def problem_61():
    """
    Cyclical figurate numbers
    循环的多边形数
    """
    test_func = [_int.is_triangle,
                 _int.is_square,
                 _int.is_pentagon,
                 _int.is_hexagon,
                 _int.is_heptagon,
                 _int.is_octagon
                 ]

    def rec_test(test_num, _func):
        """递归判断
        """
        if not test_num:
            return True
        num = test_num.pop(0)
        for func in _func:
            if func(num):
                _func.remove(func)
                return rec_test(test_num, _func)
        return False

    test = []
    numbers = range(10, 100)

    for i in itertools.combinations(numbers, 2):
        num = int(''.join(str(j) for j in i))
        if any([func(num) for func in test_func]):
            test.append(i)
        num2 = int(''.join(str(j) for j in i[::-1]))
        if any([func(num2) for func in test_func]):
            test.append(i[::-1])
    _graph = {}
    for i in test:
        if i[0] in _graph:
            _graph[i[0]].append(i[1])
        else:
            _graph[i[0]] = [i[1]]

    def find_path(_graph, start, path=[]):
        path = path + [start]
        if len(path) > 6:
            return []
        if len(path) > 5 and path[0] in _graph[start]:
            return [path]
        if start not in _graph:
            return []
        paths = []
        for node in _graph[start]:
            if node not in path:
                newpaths = find_path(_graph, node, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
    for i in _graph:
        paths = find_path(_graph, i)
        for path in paths:
            num = [int(str(path[i]) + str(path[i + 1])) for i in range(5)]
            num.append(int(str(path[-1]) + str(path[0])))
            if rec_test([i for i in num], [i for i in test_func]):
                return sum(num)


def problem_65():
    l_t=[2]+[1]*99
    if (len(l_t)-1)%3==2:
        l_t[2::3]=[i*2 for i in range(1,(len(l_t)-1)//3+2)]
    else:
        l_t[2::3]=[i*2 for i in range(1,(len(l_t)-1)//3+1)]
    #print(l_t)
    l_t.reverse()
    l_result=[1,l_t[0]]
    del l_t[0]
    #print(l_result)

    for i in l_t:
        l_result[0]=i*l_result[1]+l_result[0]
        l_result.reverse()
        #print(l_result)
    l_result.reverse()
    print(l_result)
    i_sum=0
    for i in str(l_result[0]):
        i_sum+=int(i)
    print(i_sum)


def problem_67():
    """
    Maximum path sum II
    最大路径和 II
    """
    binary_tree = list(
        map(int, i.split())
        for i in data.openfile('p067_triangle.txt').strip().splitlines())

    def helper(tree, leaf):
        LOG.debug(leaf)
        if len(leaf) == 1:
            return leaf
        else:
            root = tree.pop(-1)
            for idx, num in enumerate(root):
                left = num + leaf[idx]
                right = num + leaf[idx + 1]
                root[idx] = max([left, right])
            leaf = root
            return helper(tree, leaf)

    leaf = binary_tree.pop(-1)
    return helper(binary_tree, leaf)[0]


def problem_70():
    """
    Totient permutation
    欧拉总计函数与重排
    result = p1 * p2 * p3 * pr / (p1 - 1) * (p2 -1) * (p3 -1) * (pr - 1)
    为了result最小，分母需要最小，最小是两个数值
    > num / phi = p1 * p2 / (p1 - 1) * (p2 * 1)
    > phi = max((p1 -1) * (p2 * 2))
    """
    min_result = 10000000
    min_num = 0
    primes = [i for i in itertools.takewhile(lambda x: x <= 5000, _int.prime_sieve()) if i > 2000]
    for i in itertools.combinations(primes, 2):
        num = i[0] * i[1]
        if num > 10000000:
            continue
        phi = (i[0] - 1) * (i[1] - 1)
        if sorted(str(num)) == sorted(str(phi)):
            radio = num * 1.0 / phi
            if min_result > radio:
                min_num = num
                min_result = radio
    return min_num


def problem_71():
    a=[1,1]
    limit=1000000
    i=limit-1
    j=limit//7*3
    while a!=[j,i]:
        if a[0]/a[1]<3/7:
            a[0]+=1
        else:
            a[1]+=1
    return a[0]-1

def problem_74():
    i_result=0
    fac_temp=[1,1,2,6,24,120,720,5040,40320,362880]
    for i in range(1,1000000):
        n=0
        i_sum=i
        s_set=set()
        s_set.add(i)
        while n<59:
            #temp=str(i_sum)
            i_sum=sum(fac_temp[int(j)] for j in str(i_sum))
            #for j in temp:
            #    i_sum+=fac_temp[int(j)]
            if i_sum in s_set:break
            else:s_set.add(i_sum)
            #s_set.add(i_sum)
            n+=1
        #if len(s_set)==60:
        #    i_result+=1
        else:i_result+=1
    return i_result






