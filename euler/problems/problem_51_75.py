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
    def bin_test(test_num, _func):
        """递归判断
        """
        if not test_num:
            return True
        num = test_num.pop(0)
        for func in _func:
            if func(num):
                _func.remove(func)
                return bin_test(test_num, _func)
        return False

    test_func = [_int.is_triangle,
                 _int.is_square,
                 _int.is_pentagon,
                 _int.is_hexagon,
                 _int.is_heptagon,
                 _int.is_octagon
                 ]

    test = []
    for i in itertools.combinations(range(10, 100), 2):
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

    for i in _graph:
        paths = graph.find_ring_path(_graph, i, [], 6)
        for path in paths:
            num = [int(str(path[i]) + str(path[i + 1])) for i in range(5)]
            num.append(int(str(path[-1]) + str(path[0])))
            if bin_test([i for i in num], [i for i in test_func]):
                return sum(num)


def problem_62():
    """
    Cubic permutations
    立方数重排
    """
    cubic_map = {}
    for i in itertools.count(1):
        cubic = ''.join(sorted(str(i ** 3)))
        if cubic in cubic_map:
            cubic_map[cubic].append(i)
        else:
            cubic_map[cubic] = [i]
        if len(cubic_map[cubic]) == 5:
            LOG.debug(cubic_map[cubic])
            return min(cubic_map[cubic]) ** 3


def problem_63():
    """
    Powerful digit counts
    幂次与位数
    关键是无限接近于10，到10后就不满足条件了
    """
    count = 0
    for n in itertools.count(1):
        start = (10 ** (n - 1)) ** (1.0 / n)
        start = int(math.ceil(start))
        # end = (10 ** n - 1) ** (1.0 / n)
        # end = int(math.floor(end))
        if start == 10:
            return count
        count += 10 - start


def problem_64():
    """
    Odd period square roots
    奇周期平方根
    同类问题：
    """
    def process(start, end, num, path=[]):
        path.append(start)
        if num == end:
            return path
        num[0] = num[1] - num ** 2
        if num[0] < num[1]:
            pass
        else:
            num[0] = num % num[0]
        return process(start, end, num, path)


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


def problem_66():
    """
    Diophantine equation
    丢番图方程
    """
    max_x = 0
    for d in range(2, 1001):
        _sqrt = math.sqrt(d)
        if _sqrt == int(_sqrt):
            continue
        for y in itertools.count(2):
            x = math.sqrt(y ** 2 * d + 1)
            if int(x) == x:
                print x, d, y
                max_x = max(x, max_x)
                break
    return max_x


def problem_67():
    """
    Maximum path sum II
    最大路径和 II
    """
    binary_tree = list(
        map(int, i.split())
        for i in data.get_file('p067_triangle.txt').strip().splitlines())

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


def problem_68():
    """
    Magic 5-gon ring
    魔力五边形环
    """
    # 直接用纸和笔算出
    # 1，计算最小值(里面是12345）和最大值(里面是678910) 得出 14 <= x <= 21
    # 2，想要的最大值，则678910应该在外面,从6开始
    # 3，10要凑14，必须是1,3，如下
    return '6531031914842725'


def problem_69():
    """
    Totient maximum
    欧拉总计函数与最大值
    """
    maximum = [0, 0]
    for i in range(2, 1000001):
        phi = i * 1.0 / _int.phi(i)
        if phi > maximum[0]:
            maximum[0] = phi
            maximum[1] = i
    return maximum[1]


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
    """
    Ordered fractions
    有序分数
    """
    limit = 3 * 1.0 / 7
    min_fraction = [1, 0, 0]
    n, d = 1, 2
    while d <= 1000000:
        r = n * 1.0 / d
        if r < limit:
            if limit - r < min_fraction[0]:
                min_fraction = limit - r, n, d
            n += 1
        else:
            d += 1
    return min_fraction[1]


def problem_72():
    """
    Counting fractions
    分数计数
    就是计算欧拉函数PHI
    """
    return sum(_int.phi(i) for i in range(2, 1000001))


def problem_73():
    """
    Counting fractions in a range
    分数有范围计数
    算法同71题
    """
    fractions_count = 0
    for n in itertools.count(1):
        start = 2 * n + 1
        if start > 12000:
            return fractions_count
        for d in range(start, 3 * n):
            if d > 12000:
                continue
            if calc.gcd(n, d) == 1:
                fractions_count += 1


def problem_74():
    """
    Digit factorial chains
    数字阶乘链
    """
    factorials = [math.factorial(i) for i in range(10)]

    def chain(num):
        visited = [num]
        while True:
            num = sum(factorials[int(i)] for i in str(num))
            if num not in visited:
                visited.append(num)
                continue
            return visited
    return len([1 for i in range(1, 1000000) if len(chain(i)) == 60])


def problem_75():
    """
    Singular integer right triangles
    唯一的整数边直角三角形
    分析：
    1，最长边必须小于0.5周长，
    2，周长必须是偶数
    3, 第一个数是奇数，后面2个数必由一个是奇数
    """
    def triangles(perimeter):
        result = False
        end = int(math.floor(perimeter * 1.0 / 2))
        for a in range(1, end):
            for b in range(max(end - a, a + 1), end):
                c = perimeter - a - b
                if a ** 2 + b ** 2 == c ** 2:
                    if not result:
                        result = True
                    else:
                        return False
                    # yield (a, b, c)
        return result

    def test():
        for perimeter in range(12, 150, 2):
            right = [i for i in triangles(perimeter)]
            if right:
                print perimeter, right
    # test()
    return len([1 for i in range(12, 1500, 2) if triangles(i)])
