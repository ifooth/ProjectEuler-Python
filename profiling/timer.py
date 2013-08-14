# encoding=utf-8
'''
Created on Jun 12, 2012

@author: Joe Lei
时间测试
'''
import logging
import argparse
from timeit import Timer
import os.path
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../euler'))
sys.path.append(path)

from problems import Problem

log=logging.getLogger(__file__)

def run_timer(num):
    Problem(num).run()  

if __name__=="__main__":
    t = Timer('run_timer(2)', setup='from __main__ import run_timer')
    print(t.timeit())
        