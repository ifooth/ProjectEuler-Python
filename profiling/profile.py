'''
Created on Jun 12, 2012

@author: Joe Lei
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
    
def euler_profile():
    cProfile.run('Problem(2).run()')

if __name__=="__main__":
    euler_profile()
        