import time
class Animal(object):
    def __init__(self,name):
        print('__init__function was called')
        self.__name = name
    def __del__(self):
        print('__del__ function was called')
        print('{}對象馬上就要被幹掉了'.format(self.__name))
        
cat = Animal("波斯貓")
cat2 = cat
cat3 = cat
print(id(cat))
print(id(cat2))
print(id(cat3))
print('---馬上刪除cat對象')
del cat
print('---馬上刪除cat2對象')
del cat2
print('---馬上刪除cat3對象')
del cat3

