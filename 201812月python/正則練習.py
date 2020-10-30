import re
s = 'The dai is sunny'
res = re.search('^The.*sunny$',s)
print(res.group())


res = re.findall('[a-m]',s)
print(res)


x = re.search("\s", s)
print(x.span())

str = "The rain in Spain"
x = re.split("\s", str) #maxsplit 
print(x)

str = "The rain in Spain A"
x = re.sub("\s", "9", str,3)
print(x)

foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
res=sorted(foo,key=lambda x:x)      #abs()函数返回绝对值,传两个条件，x<0和abs(x)
print(res)    
res2 = sorted(foo,key = lambda x:abs(x),reverse = False)
print(res2)
