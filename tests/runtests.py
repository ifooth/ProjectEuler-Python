'''
Created on Jun 12, 2012

@author: Joe Lei
'''
import unittest
import os.path
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../euler'))
sys.path.append(path)

from problems import Problem

class Test_25(unittest.TestCase):


    def test_problem_1(self):
        self.assertEqual(233168, Problem(1).run())

if __name__ == "__main__":   
    unittest.main()