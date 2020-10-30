a =[1,2]
b =[3,4]
res = [i for i in zip(a,b)]
print(res)


a = 'xy'
b = 'abc'
res = [i for i in zip(a,b)]
print(res)
'''
zip()函数在运算时，会以一个或多个序列（可迭代对象）
做为参数，返回一个元组的列表。同时将这些序列中并排的元素配对。
'''
