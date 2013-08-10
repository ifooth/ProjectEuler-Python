'''
Created on 2012-7-18

@author: botwave
'''

def triangle(n):
    """ euler problem 45
    
    """
    return n*(n+1)//2

def pentagonal(n):
    """ euler problem 44
    Pentagonal numbers are generated by the formula, Pn=n(3n1)/2. The first ten pentagonal numbers are:
    1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
    
    >>> pentagonal(5)
    """
    return n*(3*n - 1)//2

def hexagonal(n):
    """euler problem 45
    
    """
    return n*(2*n-1)
import math
def is_integer(x,epsilon=1e-6):
    """Return True if the float x "seems" an integer"""
    return (abs(round(x) - x) < epsilon)

def is_pentagonal(n):
    """ euler problem 44
    Pentagonal numbers are generated by the formula, Pn=n(3n1)/2. The first ten pentagonal numbers are:
    1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
    """
    return (n >= 1) and is_integer((1+math.sqrt(1+24*n))/6.0)

def is_pandigital(n):
    """ euler problem 32
    
    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
    for example, the 5-digit number, 15234, is 1 through 5 pandigital.
    >>> is_pandigital(391867254)
    True
    """
    #print(locals())
    return sorted(str(n))==sorted('123456789')
def binomial(n,k):
    nt=1
    for t in range(min(k,n-k)):
        nt*=(n-t)//(t+1)
    return nt
def nCr(n,r):
    """
    combinatio
    """
    ncr=1
    for t in range(min(r,n-r)):
        ncr*=(n-t)//(t+1)
    return ncr
def nAr(n,r):
    """
    arrangement
    permutation
    """
    nar=1
    for t in range(r):
        nar*=(n-t)
    return nar
def nHr(n,r):
    pass
def test():    
    import doctest
    doctest.testmod()
if __name__=="__main__":
    test()
    #print(factors(4648767868))
