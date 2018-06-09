#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from testDemo import IntegerArimeticTest
from HTMLTestRunner import *

def add(a,b):
	return a+b

def minus(a,b):
	return a-b

def multi(a,b):
	return a*b

def divide(a,b):
	return a/b


if __name__ == '__main__':
	suit=unittest.TestSuite()
	tests=[IntegerArimeticTest("testAdd"),IntegerArimeticTest("testminus"),IntegerArimeticTest("testmulti"),IntegerArimeticTest("testdivide")]
	suit.addTests(tests)
	runner=unittest.TextTestRunner(verbosity=2)
	runner.run(suit)
	with open('HtmlReport.html', 'w') as f:
		runner=HTMLTestRunner(stream=f,title='MathFunc Test Report',description='generated by HTMLTestRunner.',verbosity=2)
		runner.run(suit)
	    
    


