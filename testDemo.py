#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest

# unittest.TestCase
# 测试的标识成功是 . 失败是 F ,跳过是s 出错是E

def add(a,b):
	return a+b

def minus(a,b):
	return a-b

def multi(a,b):
	return a*b

def divide(a,b):
	return a/b

class IntegerArimeticTest(unittest.TestCase):
	"""docstring for IntegerArimeticTest"""
	@classmethod
	def setUpClass(cls):
		print "firstly this setUpclass() only called once"
	@classmethod
	def tearDownClass(cls):
		print "finally:This tearDownClass() method only called once too."
	def setUp(self):
		print "do something before test.Prepare environment."
	def tearDown(self):
		print "do something after test.Clean up."
	def testAdd(self):
		'''test add function'''
		print 'test add'
		self.assertEqual(3,add(1,2))
		
	def testminus(self):
		''' test minus'''
		print "test minus"
		self.assertNotEqual(2,minus(4,1))
	def testmulti(self):
		self.skipTest("do not run this")
		print "test multi"
		self.assertEqual(25,multi(5,5))


	@unittest.skip("i do not want to run this case")
	def testdivide(self):
		print "test divide"
		'''test divide function'''
		self.assertEqual(2,divide(5,2))
		self.assertEqual(1,divide(2,2))



if __name__ == '__main__':
	unittest.main(verbosity=2)  # 会调用TextTestRunner中的run方法来运行testsuite

        # verbosity=2将输出每个测试用例的检查结果
    
     	'''testAdd (__main__.IntegerArimeticTest) ... ok
		   testdivide (__main__.IntegerArimeticTest) ... FAIL
		   testminus (__main__.IntegerArimeticTest) ... ok
		   testmulti (__main__.IntegerArimeticTest) ... ok

    '''


'''
 .F..     4个测试用例 成功，失败，成功，成功   出错是 E，跳过是 S
 测试执行给方法的顺序没有关系 testdivide是在第四个方法但确是第二个执行

 每个方法都要以test开头，否则不会被unittest识别
 去掉方法前面的test就会少一个testcase


======================================================================
FAIL: testdivide (__main__.IntegerArimeticTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\admin\Desktop\resource\checklist\testServer\main.py", line 30, in testdivide
    self.assertEqual(2.5,divide(5,2))
AssertionError: 2.5 != 2

----------------------------------------------------------------------
Ran 4 tests in 0.001s



在unittest.main()中加 verbosity 参数可以控制输出的错误报告的详细程度，默认是 1，如果设为 0，则不输出每一用例的执行结果，即没有上面的结果中的第1行；如果设为 2，则输出详细的执行结果，如下

可以看到，每一个用例的详细执行情况以及用例名，用例描述均被输出了出来（在测试方法下加代码示例中的”“”Doc String”“”，在用例执行时，会将该字符串作为此用例的描述，加合适的注释能够使输出的测试报告更加便于阅读）
'''