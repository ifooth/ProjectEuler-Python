# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>
from collections import Counter
import itertools
import logging
import math

from euler.lib import data
from euler.lib import _int
from euler.lib import calc


LOG = logging.getLogger(__name__)


def eight_prime_family(prime,rd):
    c=0
    for digit in '0123456789':
        n=int(prime.replace(rd,digit))
        if (n>100000 and intx(n).isPrime()):
            c=c+1
    return c==8


def problem_51():
    """
    Prime digit replacements
    素数数字替换
    """
    for prime in _int.prime_sieve():
        if prime>100000:
            s=str(prime)
            last_digit=s[5:6]
            if (s.count('0')==3 and eight_prime_family(s,'0') or \
                s.count('1')==3 and last_digit!='1' and eight_prime_family(s,'1') or \
                s.count('2')==3 and eight_prime_family(s,'2')):return s


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
    #return sum(int(i) for i in (str(a**b) for a in range(1,100) for b in range(1,100)))
    i_result=0
    for i in range(1,100):
        for j in range(1,100):
            i_result=max(i_result,sum(int(k) for k in str(i**j)))
    return i_result

def problem_57(num=1000):
    from fractions import Fraction
    init = Fraction(1,2)
    n = 0
    for i in range(num-1):
        init = 1/(2 + init)
        #log.info(init+1)
        if len(str((init+1).numerator))>len(str((init+1).denominator)):
            n+=1
    return n

def problem_58(length=None):
    if length:
        for i in range(length):
            pass

def problem_59(keychars='abcdefghijklmnopqrstuvwxyz',keylen=3):
    ciphertext=list(data.openfile('cipher1.txt').strip().split(','))
    #ciphertext=encipher('leijiaominabc','zzz')
    #log.info(encipher('leijiaominabc','zzz'))
    #log.info(ciphertext)
    log.info(len(ciphertext))
    texts = ['',0]
    a,b=divmod(len(ciphertext),keylen)
    for i in itertools.product(keychars,repeat=keylen):
        cleartext = ''
        space = 0
        for j in range(a):
            for k in range(keylen):
                t = int(ciphertext[keylen*j+k])^ord(i[k])
                if t == ord(' '):
                    space += 1
                cleartext += chr(t)
        if b:
            for k in range(b):
                t = int(ciphertext[keylen*a+k])^ord(i[k])
                if t == ord(' '):
                    space += 1
                cleartext += chr(t)
        if space > texts[1]:
            texts[1] = space
            texts[0] = cleartext
    log.info(texts)
    return sum([ord(i) for i in texts[0]])

def encipher(texts,key):
    #log.info(texts)
    #log.info(key)
    ciphertext = []
    a,b = divmod(len(texts),len(key))
    for i in range(a):
        ciphertext += [ord(texts[i*len(key)+j])^ord(key[j]) for j in range(len(key))]
    if b:
        ciphertext += [ord(texts[a*len(key)+j])^ord(key[j]) for j in range(b)]
    return ciphertext




def problem_62():
    l_lis=[]
    for i in range(1,20000):
        l_lis.append(i**3)
    #l_lis=set(l_lis)
    l_result=[0,0,0,0,0]
    for m in l_lis:
        n=0
        for j in l_lis:
            if sorted(str(m))==sorted(str(j)):
                l_result[n]=j
                n+=1
                if n==5:
                    print(l_result)
                    return m
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






