'''
Created on May 26, 2012

@author: Joe Lei
'''

import logging

from euler.problems import Problem


log = logging.getLogger('__main__')

    
if __name__=="__main__":
    FORMAT = '%(asctime)s %(module)s:%(lineno)s [%(levelname)s]:%(message)s'
    handler=logging.StreamHandler()
    handler.setFormatter(logging.Formatter(FORMAT))
    log.addHandler(handler)
    log.setLevel(logging.DEBUG)

    result=Problem(2).run()
    log.info(result)     
    
    
    
    