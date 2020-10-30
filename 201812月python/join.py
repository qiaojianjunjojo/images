
str = 'i have a dream!' #去除空格
li= str.split(" ")
print(''.join(li))

a = [i for i in range(3)]
print(type(a))

a = (i for i in range(3))
print(type(a))

'''
使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，
输出结果为[0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大
'''

foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
res = sorted(foo ,key =lambda x :-x)
print(res)

dic = {"name":"zs","sex":"man" ,"city":"bj"}
print(dic.items())
b= sorted(dic.items(),key = lambda x :x[1])
print(b)
new_dic = {i[0]:i[1] for i in b}
print(new_dic)
