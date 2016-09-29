# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
import collections
import fractions
import functools
import itertools
import logging
import math
import operator
import re


LOG = logging.getLogger(__name__)


class IntX(long):

    @property
    def is_prime(self):
        """改进的素数检测法
        """
        if self < 2:
            return False
        if self % 2 == 0 and self != 2:
            return False
        if self % 3 == 0 and self != 3:
            return False
        if any((self % i) == 0 or (self % (i + 2)) == 0 for i in range(5, int(self ** 0.5) + 2, 6)):
            return False
        return True

    def next_prime(self):
        if self & 1:
            a = self + 2
        else:
            a = self + 1
        while(not IntX(a).is_prime()):
            a += 2
        return a

    def sieve_prime(self):
        """
        Sieve of Eratosthenes
        """
        prime_list = list(range(2, self + 1))
        i = 1
        while prime_list[i-1]**2<self:
            prime_list=prime_list[:i]+list(filter(lambda k:k%prime_list[i-1],prime_list[i:]))
            i+=1
        return prime_list

    @property
    def is_palindromic(self):
        """回文数 9009
        """
        return str(self) == str(self)[::-1]

    def factors_generator(self):
        """因子生成器
        12 = 1 * 2 * 2 * 3
        """
        yield 1
        i, limit = 2, self**0.5
        while i <= limit:
            if self % i == 0:
                yield i
                self //= i
                limit = self**0.5
            else:
                i += 1
        if self > 1:
            yield self

    def factors(self):
        """
        因数分解 12 = 1^1 * 2^2 * 3^1
        return {1: 1, 2: 2, : 3: 1}
        """
        counter = collections.Counter(self.factors_generator())
        result = dict(counter)
        LOG.debug('%s factors is: %s', self, result)
        return result

    def sumOfDivisors(self):
        """
        counts the number of positive integers less than or equal to n that are relatively prime to n
        """
        assert self>0,"I must be a positive integer and must be exceed 1"
        if self==1:return 0
        i_sum=1
        for key,value in self.factors().items():
            i_sum*=sum(key**i for i in range(value+1))
        return i_sum//2-self

    def numberOfDivisors(self):
        """
        number of divisors
        """
        assert self>0
        if self==1:return 1
        else:i_sum=1
        for value in self.factors(self).values():
            i_sum*=(value+1)
        return i_sum//2

    def phi(self):
        i_result=1
        d_temp=self.factors()
        d_temp.pop(1)
        for key,value in d_temp.items():
            i_result*=(key**value-key**(value-1))
        return i_result
    def divisors(self):
        l_temp=self.factors()
        del l_temp[0]
        l_a=[]
        i_len=len(l_temp)
        i=0
        while i<i_len:
            j=1
            l_a.append([1])
            while j<=l_temp[i][1]:
                l_a[i].append(l_temp[i][0]**j)
                j+=1
            i+=1
            j=1
            l_result=l_a[0]
            while j<len(l_a):
                l_te=[]
                for t_m in l_a[j]:
                    for t_n in l_result:
                        l_te.append(t_m*t_n)
                        l_result=l_te
                        j+=1
        return l_result


class fractionx(fractions.Fraction):
    def __new__(cls,s):
        self=super(XFraction,cls).__new__(cls)
        r=re.compile('^-?[0-9]*(\.[0-9]*(\([1-9]+[0-9]*\))?)?$')
        mat=r.match(s)
        try:
            self.xf=mat.group()
        except:
            raise IndexError
        else:
            return self
        #super(xfraction.self).__init__(self) python 2x
        #else:fractions.Fraction.__new__(self)

    def toFraction(self):
        a=re.search('-?[0-9]*',self.xf)
        if a:
            a=a.group()
        else:
            a=0
        b=re.search('\.[0-9]*',self.xf)
        if b:
            b=b.group()[1:]
        else:
            b=''

        repeat=re.search('\([1-9]+[0-9]*\)',self.xf)
        if repeat:
            repeat=repeat.group()[1:-1]
        else:
            repeat=''
        if repeat is '':
            self.XF=fractions.Fraction(self.xf)
        else:
            if b is '':
                self.XF=fractions.Fraction(a)+fractions.Fraction(repeat+'/'+'9'*len(repeat))
            else:
                self.XF=fractions.Fraction(a)+fractions.Fraction(str(int(b+repeat)-int(b))+'/'+'9'*len(repeat)+'0'*len(b))
        return self.XF

    def toRepeatingDecimal(self):
        """长除法
        """
        a=self.numerator()
        b=self.denominator()
        l=[divmod(a,b)]
        k=10*len(b)*l[0][1]
        i=0
        temp=divmod(k,b)
        while temp not in l or l[-1][0]==0:
            l.append(temp)
            i+=1
            k=10*len(b)*l[i][1]
            temp=divmod(k,b)
        return l


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
    return str(num) == str(num)[::-1]


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
    counter = collections.Counter(factors_generator(num))
    result = dict(counter)
    LOG.debug('%s factors is: %s', num, result)
    return result


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
        fib_n = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib_n
        yield fib_n


def is_pandigital(num, n=9):
    """
    全数字
    """
    n_letters = '123456789'
    str_num = str(num)
    set_num = set(str_num)
    if len(str_num) != len(set_num):
        return False
    return n_letters[:n] == ''.join(sorted(set_num))
