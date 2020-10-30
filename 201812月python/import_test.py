import Recursion_test
print(Recursion_test.digui(7))
print(__name__)
"""
迭代器协议（iterator protocol）是指要实现对象的 __iter()__ 和 next() 方法
（注意：Python3 要实现 __next__() 方法），其中，__iter()__ 方法返回迭代器对
象本身 return self ，next()方法返回容器的下一个元素 return a，在没有后续元素时
抛出 StopIteration 异常。
"""
