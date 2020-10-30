import json
x='{"a":1,"b":2,"c":3}'
y=json.loads(x)
print(y)
print()
            
"""
迭代器协议（iterator protocol）是指要实现对象的 __iter()__ 和 next() 方法
（注意：Python3 要实现 __next__() 方法），其中，__iter()__ 方法返回迭代器对
象本身 return self ，next()方法返回容器的下一个元素 return a，在没有后续元素时
抛出 StopIteration 异常。
"""
x2={"class1":100,"class2":80,"class3":60}
y2=json.dumps(x2)
print(y2)
print()


x = {
  "name": "John","age": 30,"married": True,
  "divorced": False, "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4, separators=(",", " = "),sort_keys=False))

