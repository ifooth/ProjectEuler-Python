# encoding=utf-8
'''
Created on Jun 12, 2012

@author: Joe Lei
性能测试
'''
import logging
import cProfile
import pstats
import os.path
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../euler'))
sys.path.append(path)

from problems import Problem

log=logging.getLogger(__file__)
    
def euler_profile(num=1):
    p = 'Problem(%s).run()' % num
    cProfile.run(p)

if __name__=="__main__":
    euler_profile()
        