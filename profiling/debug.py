# encoding=utf-8
'''
Created on Jun 12, 2012

@author: Joe Lei
调试器
'''
import pdb
import os.path
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../euler'))
sys.path.append(path)

from problems import Problem

if __name__=="__main__":
    pdb.run('Problem(2).run()')