'''
Created on 2012-7-18

@author: botwave
'''

import math


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
