# encoding=utf-8
'''
Created on Jun 12, 2012

@author: Joe Lei
时间测试
'''
import logging
from timeit import Timer
import os.path
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../euler'))
sys.path.append(path)

from problems import Problem

log=logging.getLogger(__file__)

def euler_test():
    Problem(2).run()  

if __name__=="__main__":   
    
    t = Timer('euler_test()', setup='from __main__ import euler_test')
    print(t.timeit())
        