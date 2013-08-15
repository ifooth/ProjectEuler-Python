# encoding=utf-8
'''
Created on May 26, 2012

@author: Joe Lei
'''

import logging
import argparse

from euler.problems import Problem
from profiling import profile

log = logging.getLogger('__main__')


def main():
    FORMAT = '%(asctime)s %(module)s:%(lineno)s [%(levelname)s]:%(message)s'
    handler=logging.StreamHandler()
    handler.setFormatter(logging.Formatter(FORMAT))
    log.addHandler(handler)
    log.setLevel(logging.DEBUG)
    
    parser = argparse.ArgumentParser(description='euler commander')    
    parser.add_argument('problem', metavar='num', type=int, nargs=1,
                   help='problem num')
    parser.add_argument('--test', metavar='num', type=int, nargs=1,
                        help='test num')
    parser.add_argument('--profile',metavar='num', type=int, nargs=1,
                        help='profile num')
    args = parser.parse_args()
    if args.problem:
        result = Problem(args.problem[0]).run()
        log.info(result)
    if args.profile:
        profile.euler_profile(args.profile[0])
    if args.test:
        pass
    
if __name__=="__main__":   
    main()     
    
    
    
    